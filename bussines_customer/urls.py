from django.urls import path
from bussines_customer import views

urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("index/", views.index, name="index"),
    path("get_requests/<status>/", views.get_requests, name="get_requests"),
    path("new_request/", views.new_request, name="new_request"),
    path("requests/", views.requests, name="requests"),
    path("view_request/<id>/", views.view_request, name="view_request"),
]