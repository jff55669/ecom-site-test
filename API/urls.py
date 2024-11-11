# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('order/', views.OrderList.as_view(), name='Order_List'),
#     path('user/', views.UserList.as_view(), name='User_List'),
#     path('product/', views.ProductList.as_view(), name= 'Product_List'),
#     path('user/<int:pk>', views.UserUpdate.as_view(), name='User_Update'),
#     path('order/<int:pk>', views.OrderUpdate.as_view(), name='Order_Update'),
#     path('product/<int:pk>', views.ProductUpdate.as_view(), name='Product_Update'),
    
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, UserViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
