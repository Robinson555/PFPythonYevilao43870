from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages as messages_module
from .models import Message
from .forms import MessageForm

@login_required
def messages_view(request):
    form = MessageForm()
    received_messages = Message.objects.filter(receiver=request.user)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            msg = Message(sender=request.user, receiver=info['receiver'], content=info['content'])
            msg.save()
            messages_module.success(request, "Message Sent")
            form = MessageForm()
        else:
            messages_module.error(request, "Message Not Sent")
    return render(request, 'messages.html', {'form': form, 'received_messages': received_messages})