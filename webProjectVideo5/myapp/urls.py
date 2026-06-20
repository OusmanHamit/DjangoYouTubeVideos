from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('prodcut/add/', views.add_product, name='add_product'),
    path('product/<int:pk>/update/', views.update_product, name='update_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
]
