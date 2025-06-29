from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('voting/', views.voting, name='voting'),
    path('results/', views.results, name='results'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('admin/login/', views.admin_login, name='admin_login'),
]
