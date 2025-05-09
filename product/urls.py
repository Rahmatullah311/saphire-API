from django.urls import path
from . import views



urlpatterns = [
  path('product/', views.ProductListCreateAPIView.as_view(), name='products'),
  path('product/<int:pk>', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-product'),
]