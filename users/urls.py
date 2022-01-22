from django.urls import path
from .views import HomeView, RegisterView , LoginView , UserView , LogoutView

urlpatterns = [
     path('' ,HomeView.as_view() ),

    path('register', RegisterView.as_view()),
    path('login' , LoginView.as_view()),
    path('user' , UserView.as_view()),
    path('logout' , LogoutView.as_view())
]
