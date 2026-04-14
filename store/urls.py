from django.urls import path
from . import views

urlpatterns = [
    
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('', views.store, name='store'),  # 👈 ye important hai
    path('search/', views.search, name='search'),
    path('place-order/', views.place_order, name='place_order'), 
    

   
]
