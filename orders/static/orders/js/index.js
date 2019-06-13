document.addEventListener('DOMContentLoaded', () => {

  // Initial settings

  document.querySelector('#selectedpizzaandsub').style.display = "block";
  document.querySelector('#selectedothers').style.display = "none";

  document.querySelector('#selectedpizza').style.display = "block";
  document.querySelector('#selectedsub').style.display = "none";

  getpizza(document.querySelector('#pizzatype').value);

  document.querySelector('#selectedpastasalad').style.display = "block";
  document.querySelector('#selecteddinnerplatter').style.display = "none";

  //  ----

  document.querySelector('#pizzaorothers').onchange = function(){
    var selected = document.querySelector('#pizzaorothers').value;

    if(selected == "pizzaandsub")
    {
      document.querySelector('#selectedpizzaandsub').style.display = "block";
      document.querySelector('#selectedothers').style.display = "none";
    }
    else if(selected=="others")
    {
      document.querySelector('#selectedpizzaandsub').style.display = "none";
      document.querySelector('#selectedothers').style.display = "block";
    }
  };

  // For pizza and sub selection
  document.querySelector('#pizzaorsub').onchange = function(){
    var selected = document.querySelector('#pizzaorsub').value;

    if(selected == "pizza")
    {
      document.querySelector('#selectedpizza').style.display = "block";
      document.querySelector('#selectedsub').style.display = "none";
    }
    else if(selected=="sub")
    {
      document.querySelector('#selectedpizza').style.display = "none";
      document.querySelector('#selectedsub').style.display = "block";
      getsubs();
    }
  }

  // For pasta/salad or dinner platter selection
  document.querySelector('#others').onchange = function(){
    var selected = document.querySelector('#others').value;

    if(selected == "pastasalad")
    {
      document.querySelector('#selectedpastasalad').style.display = "block";
      document.querySelector('#selecteddinnerplatter').style.display = "none";
    }
    else if(selected=="dinnerplatter")
    {
      document.querySelector('#selectedpastasalad').style.display = "none";
      document.querySelector('#selecteddinnerplatter').style.display = "block";
    }
  }

  document.querySelector('#pizzatype').onchange = () => {
    getpizza(document.querySelector('#pizzatype').value);
  };
});

function getsubs()
{
  $.ajax({
    url : '/ajax/getmenuinfo',
    data : {
      'data' : 'sub'
    },
    dataType : 'json',
    success : function(data){
      var sel = document.querySelector('#subname');
      sel.innerHTML = '';
      data.subnames.forEach(function(sub){
        var opt = document.createElement('option');
        opt.appendChild(document.createTextNode(sub));
        opt.value = sub.toLowerCase();
        sel.appendChild(opt);
      });

      // Toppings for pizza
      var extrasel = document.querySelector('#subextra');
      extrasel.innerHTML = '';
      data.extranames.forEach(function(extra){
        var opt = document.createElement('option');
        opt.appendChild(document.createTextNode(extra));
        opt.value = extra.toLowerCase();
        extrasel.appendChild(opt);
      });
    }
  });
}

function getpizza(type)
{
  $.ajax({
    url : '/ajax/getmenuinfo',
    data : {
      'data' : 'pizza',
      'type' : type
    },
    dataType : 'json',
    success : function(data){
      // Pizza names
      var sel = document.querySelector('#pizzaname');
      sel.innerHTML = '';
      data.pizzanames.forEach(function(pizza){
        var opt = document.createElement('option');
        opt.appendChild(document.createTextNode(pizza));
        opt.value = pizza.toLowerCase();
        sel.appendChild(opt);
      });

      // Toppings for pizza
      var topsel = document.querySelector('#toppings');
      topsel.innerHTML = '';
      data.toppingnames.forEach(function(topping){
        var opt = document.createElement('option');
        opt.appendChild(document.createTextNode(topping));
        opt.value = topping.toLowerCase();
        topsel.appendChild(opt);
      });
    }
  });
}
