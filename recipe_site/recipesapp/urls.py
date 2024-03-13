from django.urls import path

from .views import login_view, register, logout_view, mock

urlpatterns = [
    path('', mock, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
