from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Conversation {self.id}"
    
    @property
    def last_message(self):
        return self.messages.order_by('-created_at').first()

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.sender.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"