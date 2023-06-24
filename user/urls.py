from django.urls import path
from .views import custom_register, custom_login, costum_logout


urlpatterns = [
    path('register/', custom_register, name="register"),
    path('login/', custom_login, name="login"),
    path("logout/", costum_logout, name="logout")
]