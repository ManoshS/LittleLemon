
from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'Booking', BookingViewSet, basename='Booking')
urlpatterns = router.urls

urlpatterns = [
    path('home/', views.home,name='home'),
    path('booking/',views.BookingView.as_view(),name='Booking'),
    path('menu/',views.ListMenuItemsView.as_view(),name="Menu"),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view(),name="MenuById"),
    path('booking/set/',include(router.urls)),
    path('RegisterUser/',views.RegisterUser.as_view()),
    path('api-token-auth/',obtain_auth_token),
]