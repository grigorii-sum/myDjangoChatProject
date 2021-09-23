from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import CreateMessageForm
from .models import Message


@login_required
def chat_page(request):
    form = CreateMessageForm()
    if request.method == 'POST':
        form = CreateMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.author_id = request.user
            message.save()

            messages = Message.objects.order_by('created_at')
            context = {
                'title': 'Чат',
                'form': form,
                'messages': messages,
            }
            return render(request, 'chatApp/chat.html', context)

    messages = Message.objects.order_by('created_at')
    context = {
        'title': 'Чат',
        'form': form,
        'messages': messages,
    }
    return render(request, 'chatApp/chat.html', context)
