from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ContactForm, SubscribeForm
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    products = Product.objects.all()
    clients = Client.objects.all()
    contact_form = ContactForm()
    subscribe_form = SubscribeForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            email_subject = f'New contact: {contact_form.cleaned_data["email"]}: {contact_form.cleaned_data["subject"]}'
            email_message = f'Name: {contact_form.cleaned_data["name"]} \nMessage: {contact_form.cleaned_data["message"]}'
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, ['srivardhan.singh.rathore@gmail.com'],
                      fail_silently=False)
            send_mail("Narayan Iron", f"Thank you {contact_form.cleaned_data['name']} for Contacting Us. \nWe will "
                                      f"revert back to you soon",
                      settings.CONTACT_EMAIL,
                      [contact_form.cleaned_data["email"]], fail_silently=False)
            return HttpResponse("Success")
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            send_mail("Narayan Iron", "You've Successfully Subscribed to our NewsLetter.", settings.CONTACT_EMAIL,
                      [subscribe_form.cleaned_data['email']], fail_silently=False)
            return HttpResponse("Success")
    else:
        context = {"products": products, "clients": clients, "form": contact_form}
        return render(request, "home/index.html", context)