from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import logging

# Create your views here.

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def send_contact_email(name, email, subject, message):
    subject = f"MESSAJ NOU - CONTACT FORM WEBSITE - DE LA -> NUME: {name}"
    body = f"Mesaj nou înregistrat de pe contact form de la NUME:  {name} \n SUBIECT: {subject} \n  EMAIL <{email}>:\n\n{message}"
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ["cheovariionut@yahoo.com"], fail_silently=False)


def handle_contact_form(request,form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message'] 

    send_contact_email(name, email, subject, message)

def home(request):


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                handle_contact_form(request, form)
                    
                messages.success(request, 'Mesajul tau a fost trimis cu succes!')
                return redirect('home')
            except Exception as e:
                logger.error(f"Error sending email: {e}")
                messages.error(request, 'A aparut o eroare la trimiterea mesajului. Te rog sa incerci din nou mai tarziu.')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error][0])

    
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


   