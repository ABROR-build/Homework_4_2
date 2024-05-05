from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/<int:pk>/', views.show_products, name='show_products'),
    path('product/<int:pk>/', views.show_product, name='show_product'),
    path('product/new/', views.add_product, name='add_product'),
    path('product/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),

]
