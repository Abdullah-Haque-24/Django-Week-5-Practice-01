from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile/pass_change/', views.pass_change, name="pass_change"),
    path('profile/without_Old_pass_change/', views.without_Old_pass_change, name="without_Old_pass_change"),
]