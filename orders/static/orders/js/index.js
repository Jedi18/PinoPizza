document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#selectedpizzaandsub').style.visibility = "";
  document.querySelector('#selectedothers').style.visibility = "hidden";
  
  document.querySelector('#pizzaorothers').onchange = function(){
    var selected = document.querySelector('#pizzaorothers').value;

    if(selected == "pizzaandsub")
    {
      document.querySelector('#selectedpizzaandsub').style.visibility = "";
      document.querySelector('#selectedothers').style.visibility = "hidden";
    }
    else if(selected=="others")
    {
      document.querySelector('#selectedpizzaandsub').style.visibility = "hidden";
      document.querySelector('#selectedothers').style.visibility = "";
    }
  };
});
