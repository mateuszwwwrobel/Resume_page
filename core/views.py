from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    form = MessageForm(request.POST or None)

    context = {
        'form': form
    }


    return render(request, 'contact.html', context)



def message_sent(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()

        sender = request.POST.get('message_name')
        subject = 'Message - ' + sender
        message_text = request.POST.get('message_text')
        mail = request.POST.get('message_email')
        
        
        send_mail(
            subject,
            message_text,
            mail,
            ['matthew.sparrow91@gmail.com'],
        )


    return render(request, 'message.html')
