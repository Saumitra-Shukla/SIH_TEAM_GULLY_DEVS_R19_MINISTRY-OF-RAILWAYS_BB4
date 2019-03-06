from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',  auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile,name='profile'),
    path('logout/',  views.logout_user,name='logout'),
    path('fav/',  views.logout_user,name='fav'),
]
