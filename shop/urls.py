from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "HomeShop"),
    path("about/", views.about, name = "AboutUs"),
    path("contact/", views.contact, name = "ContactUs"),
    path("tracker/", views.tracker, name = "TrackingStatus"),
    path("search/", views.search, name = "Search"),
    path("productview/", views.productview, name = "Productview"),
    path("checkout/", views.checkout, name = "CheckOut")

]