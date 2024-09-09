from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('travel/', views.travel_list, name='travel_list'),
    path('book/<int:travel_id>/', views.booking_form, name='booking_form'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]