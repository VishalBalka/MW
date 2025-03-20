from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages as django_messages
from django.db.models import Q
from .models import Conversation, Message
from .forms import MessageForm

@login_required
def inbox_view(request):
    conversations = Conversation.objects.filter(participants=request.user).order_by('-updated_at')
    return render(request, 'messaging/inbox.html', {'conversations': conversations})

@login_required
def conversation_view(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, participants=request.user)
    
    # Mark messages as read
    conversation.messages.filter(~Q(sender=request.user), is_read=False).update(is_read=True)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            conversation.updated_at = message.created_at
            conversation.save()
            return redirect('conversation', conversation_id=conversation.id)
    else:
        form = MessageForm()
    
    messages_list = conversation.messages.order_by('created_at')
    other_participant = conversation.participants.exclude(id=request.user.id).first()
    
    return render(request, 'messaging/conversation.html', {
        'conversation': conversation,
        'messages': messages_list,
        'form': form,
        'other_user': other_participant
    })

@login_required
def new_message_view(request, user_id):
    recipient = get_object_or_404(User, id=user_id)
    
    # Check if conversation already exists
    conversation = Conversation.objects.filter(
        participants=request.user
    ).filter(
        participants=recipient
    ).first()
    
    if conversation:
        return redirect('conversation', conversation_id=conversation.id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Create new conversation
            conversation = Conversation.objects.create()
            conversation.participants.add(request.user, recipient)
            
            # Create message
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            
            django_messages.success(request, f'Message sent to {recipient.get_full_name() or recipient.username}!')
            return redirect('conversation', conversation_id=conversation.id)
    else:
        form = MessageForm()
    
    return render(request, 'messaging/compose.html', {
        'form': form,
        'recipient': recipient
    })