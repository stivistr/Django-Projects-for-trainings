from django.urls import path, include
from Petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='pet-add'),
    path('<str:username>/pet/<slug:pet_name>', include([
        path('', views.pet_details, name='pet-details'),
        path('edit/', views.pet_edit, name='pet-edit'),
        path('delete/', views.pet_delete, name='pet-delete'),
    ]))
]