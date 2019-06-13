document.addEventListener('DOMContentLoaded', () => {

  // Initial settings

  document.querySelector('#selectedpizzaandsub').style.display = "block";
  document.querySelector('#selectedothers').style.display = "none";

  document.querySelector('#selectedpizza').style.display = "block";
  document.querySelector('#selectedsub').style.display = "none";

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
});
