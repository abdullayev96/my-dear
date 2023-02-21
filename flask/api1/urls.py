from django.urls import path
from .views import UserApiView


urlpatterns = [
    path("network/", UserApiView.as_view(), name= "User_list")
]