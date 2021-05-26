from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path("products/<int:id>", views.productview, name="Productview"),
    path("checkout/", views.checkout, name="Checkout"),
]