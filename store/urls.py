from django.urls import path
from . import views

urlpatterns = [
  path('store/', views.StoreListCreateView.as_view(), name='store-list'),
]