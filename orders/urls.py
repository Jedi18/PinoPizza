from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("menu", views.menu, name="menu"),
    path("ajax/getmenuinfo", views.getmenuinfo, name="getmenuinfo"),
    path("cart", views.cart, name="cart")
]
