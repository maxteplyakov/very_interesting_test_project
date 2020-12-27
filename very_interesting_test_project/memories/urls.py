from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('new_memory/', views.new_memory, name='new_memory'),
    path('', views.profile, name='profile'),
]