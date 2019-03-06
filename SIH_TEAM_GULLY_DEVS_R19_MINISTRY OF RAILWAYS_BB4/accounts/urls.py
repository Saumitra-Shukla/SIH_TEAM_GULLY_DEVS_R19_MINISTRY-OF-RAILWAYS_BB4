from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',  auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile,name='profile'),
    path('logout/',  auth_views.LogoutView.as_view(),name='logout'),
    path('fav/',  auth_views.LogoutView.as_view(),name='fav'),
]
