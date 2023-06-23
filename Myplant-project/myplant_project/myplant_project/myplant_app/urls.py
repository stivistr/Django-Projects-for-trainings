from django.urls import path
from myplant_project.myplant_app import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('profile/create/', views.create_profile, name='create-profile'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.create_plant, name='create-plant'),
    path('details/<int:plant_id>/', views.plant_details, name='plant_details'),
    path('edit/<int:plant_id>/', views.edit_plant, name='edit-plant'),
    path('delete/<int:plant_id>/', views.delete_plant, name='delete-plant'),
    path('profile/details/', views.profile_details, name='profile-details'),
    path('profile/edit/', views.profile_edit, name='profile-edit'),
    path('profile/delete/', views.profile_delete, name='profile-delete'),
]
