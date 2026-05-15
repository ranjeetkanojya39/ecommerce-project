from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),  
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'), 
    path('activate/<uidb64>/<token>/' , views.activate, name='activate'),  
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('my_orders/', views.my_orders, name='my_orders'),
    


]