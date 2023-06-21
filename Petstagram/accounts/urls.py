from django.urls import path, include
from Petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.show_profile_details, name='profile-details'),
        path('delete/', views.delete_profile, name='profile-delete'),
        path('edit/', views.edit_profile, name='profile-edit'),
    ]))
]