from datetime import timedelta

from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from .models import Message
from .forms import MessageForm


@login_required(login_url='/accounts/login/')
def home_view(request, author=0, time=0, reverse=False):
    """
    add a new message
    view a messages (if necessary with filter)
    """
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if not data.get('media_file'):
                data.pop('media_file')
            new_message = Message(**data, author=get_user(request))
            new_message.save()

    form = MessageForm()
    messages = Message.objects.all()
    if author:
        messages = messages.filter(author=author)
    if reverse == 'True':
        messages = messages.order_by('-create_time')
    if time:
        delta = timezone.now()-timedelta(hours=time)
        messages = messages.filter(create_time__range=(delta, timezone.now()))
    return render(request, 'chat/message_with_filter.html', {'form': form,
                                                              'messages': messages,
                                                              'author': author,
                                                              'time': time,
                                                              'reverse': reverse})
