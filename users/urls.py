from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import RegisterView, UserView, MyTokenObtainPairView

urlpatterns = [
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('users/<int:pk>/', UserView.as_view(), name='user'),
]
