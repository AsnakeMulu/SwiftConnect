from django.urls import path
from crm import views

urlpatterns = [
    path("index/", views.admin_index, name="admin_index"),
    path("get_requests/<status>/", views.get_admin_requests, name="get_admin_requests"),
    path("requests/", views.admin_requests, name="admin_requests"),
    path("view_request/<id>/", views.admin_view_request, name="admin_view_request"),
    path("approve_request/<id>/", views.approve_request, name="approve_request"),
    path("reject_request/<id>/", views.reject_request, name="reject_request"),
    path("successful/<message>/", views.successful, name="successful"),
]