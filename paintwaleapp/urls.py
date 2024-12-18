from django.urls import path

from . import views
app_name="paintwale"
urlpatterns = [
    path("", views.index, name="index"),
        path("home/", views.home, name="home"),
        path("about/", views.about, name="about"),
        path("service/",views.service, name="service"),
        path("contact/",views.contact, name="contact"),
        path("sendMessage/",views.sendMessage, name="sendMessage")


]