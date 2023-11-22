from django.urls import path
from .views import product_list, product_detail, register
from .api import CustomObtainAuthToken

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('register/', register, name='register'),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
]
