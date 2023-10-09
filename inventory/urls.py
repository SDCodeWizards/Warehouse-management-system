from django.urls import path

from . import views

urlpatterns = [
    path('', views.toLogin),
    path('login/', views.toLogin),

    path('index/', views.Login, name='production_list')
]