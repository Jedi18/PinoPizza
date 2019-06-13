from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import PizzaAndSubs, Others, ToppingsAndExtra
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
    pass

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
    return JsonResponse(data)
