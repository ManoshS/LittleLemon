
from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home,name='home'),
    path('booking/',views.BookingView.as_view(),name='Booking'),
    path('menu/',views.ListMenuItemsView.as_view(),name="Menu")
]