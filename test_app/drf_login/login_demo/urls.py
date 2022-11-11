from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AuthView, RegisterView, MyObtainTokenPairView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('auth/', AuthView.as_view(), name='auth'),
    path('register/', RegisterView.as_view(), name='register'),
]
