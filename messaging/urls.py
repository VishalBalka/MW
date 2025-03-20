from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox_view, name='inbox'),
    path('conversation/<int:conversation_id>/', views.conversation_view, name='conversation'),
    path('new/<int:user_id>/', views.new_message_view, name='new_message'),
]