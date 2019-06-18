from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Max
from .models import PizzaAndSubs, Others, ToppingsAndExtra, Orders
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message":None})

    context = {
        "user":request.user
    }
    return render(request, "orders/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        max_cartno = Orders.objects.aggregate(Max('cartno'))
        maxcart = max_cartno['cartno__max']
        latest = Orders.objects.filter(cartno = maxcart)
        # If max cart number has been ordered, set new cartno to 1 plus that
        if latest[0].ordered is True:
            maxcart += 1
        request.session["cartno"] = maxcart
        print(request.session["cartno"])
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message":"Invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message":"Logged out"})

def register_view(request):
    if request.method == "GET":
        return render(request, "orders/registration.html")

    user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
    user.first_name = request.POST["first_name"]
    user.last_name = request.POST["last_name"]
    user.save()
    return HttpResponseRedirect(reverse("index"))

def menu(request):
    #if pizza/subs
    if request.POST["pizzaorothers"] == "pizzaandsub":
        if request.POST["pizzaorsub"] == "pizza":
            pizzatype = request.POST["pizzatype"].capitalize()
            pizzaname = request.POST["pizzaname"].capitalize()
            pizzasize = request.POST["pizzasize"]
            toppings = request.POST["toppings"].capitalize()
            res = PizzaAndSubs.objects.filter(name=pizzaname,type=pizzatype).all()
            if pizzasize == 'small':
                total = res[0].small
                size = "Small"
            elif pizzasize == 'large':
                total = res[0].large
                size = "Large"
            order = "{} {} pizza with {} topping".format(pizzatype, pizzaname, toppings)
        elif request.POST["pizzaorsub"] == "sub":
            subname = request.POST["subname"].capitalize()
            subsize = request.POST["subsize"]
            subextra = request.POST["subextra"].capitalize()
            res = PizzaAndSubs.objects.filter(name=subname, type="Sub").all()
            if subsize == 'small':
                total = res[0].small
                size = "Small"
            elif subsize == 'large':
                total = res[0].large
                size = "Large"
            if subextra != 'Noextras':
                extra = ToppingsAndExtra.objects.filter(name=subextra, isextra=True).all()
                total += extra[0].price
                order = "{} sub with extra {}".format(subname, subextra)
    elif request.POST["pizzaorothers"] == "others":
        if request.POST["others"] == "pastasalad":
            pastasaladname = request.POST["pastasaladname"]
            ps = Others.objects.filter(name=pastasaladname, isdinnerplatter=False).all()
            total = ps[0].large
            order = "{} - Pasta / Salad".format(pastasaladname)
            size = None
        elif request.POST["others"] == "dinnerplatter":
            dinnerplattername = request.POST["dinnerplattername"]
            dinnerplattersize = request.POST["dinnerplattersize"]
            dp = Others.objects.filter(name=dinnerplattername, isdinnerplatter=True).all()
            if dinnerplattersize == 'small':
                total = dp[0].small
                size = "Small"
            elif dinnerplattersize == 'large':
                total = dp[0].large
                size = "Large"
            order = "{} Dinner Platter".format(dinnerplattername)

    ord = Orders.objects.create(order=order, price=total,cartno=request.session['cartno'], size=size)
    return HttpResponseRedirect(reverse("cart"))

def getmenuinfo(request):
    type = request.GET.get('data', None)

    if type == 'sub':
        subs = PizzaAndSubs.objects.filter(ispizza=False).all()
        subnames = [sub.name for sub in subs]
        extras = ToppingsAndExtra.objects.filter(isextra=True).all()
        extranames = [extra.name for extra in extras]
        data = {
            "subnames" : subnames,
            "extranames" : extranames
        }
    elif type == 'pizza':
        pizzatype = request.GET.get('type').title()
        pizzas = PizzaAndSubs.objects.filter(type=pizzatype).all()
        toppings = ToppingsAndExtra.objects.filter(isextra=False).all()
        toppingnames = [topping.name for topping in toppings]
        pizzanames = [pizza.name for pizza in pizzas]
        data = {
            "pizzanames" : pizzanames,
            "toppingnames" : toppingnames
        }
    elif type == "pastasalad":
        pastas = Others.objects.filter(type="Pasta").all()
        salads = Others.objects.filter(type="Salad").all()
        pastanames = [pasta.name for pasta in pastas]
        saladnames = [salad.name for salad in salads]
        data = {
            "pastanames" : pastanames,
            "saladnames" : saladnames
        }
    elif type == "dinnerplatter":
        dinnerplatters = Others.objects.filter(isdinnerplatter=True).all()
        dinnerplatternames = [dinnerplatter.name for dinnerplatter in dinnerplatters]
        data = {
            "dinnerplatternames" : dinnerplatternames
        }
    return JsonResponse(data)

def cart(request):
    orders = Orders.objects.filter(cartno=request.session["cartno"]).all()
    total = 0
    cart = []
    for order in orders:
        cart.append({"name":order.order,"size":order.size,"price":order.price})
        total += float(order.price)

    actualtotal = total + (total * 0.25) + 5 + 2
    return render(request, "orders/cart.html", {"cart":cart, "total":total,"actualtotal":actualtotal})

def place_order(request):
    Orders.objects.filter(cartno=request.session["cartno"]).update(ordered=True)
    request.session["cartno"] += 1
    return render(request, "orders/ordered.html")
