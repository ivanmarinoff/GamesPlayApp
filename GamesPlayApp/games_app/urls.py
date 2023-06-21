from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('profile/', include([
        path('create/', profile_create, name='profile-create'),
        path('details/', profile_details, name='profile-details'),
        path('edit/', profile_edit, name='profile-edit'),
        path('delete/', profile_delete, name='profile-delete'),
        path('dashboard/', game_dashboard, name='game-dashboard'),
    ])),

    path('game/', include([
        path('create/', game_create, name='game-create'),
        path('details/<int:pk>/', game_details, name='game-details'),
        path('edit/<int:pk>/', game_edit, name='game-edit'),
        path('delete/<int:pk>/', game_delete, name='game-delete'),
    ]))
]