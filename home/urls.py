from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-home'),
    path('add/', views.add, name='home-add'),
    path('edit/<int:aufgabe_id>', views.edit, name='home-edit'),
    path('delete/<int:aufgabe_id>', views.delete, name='home-delete'),
    path('impressum/', views.impressum, name='home-impressum'),
]
