from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile_view, name='create_profile'),
    path('edit/', views.edit_profile_view, name='edit_profile'),
    path('view/<int:profile_id>/', views.view_profile_view, name='view_profile'),
    path('browse/', views.profile_list_view, name='profile_list'),
]
