from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.index,name="homepage"),
    path("login/",views.login,name="loginpage"),
    path("register/",views.register,name="registerpage"),
    path("logout/",views.logout,name="logoutpage")
]