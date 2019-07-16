from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y direccionamos
            email = EmailMessage(
                'La caffettiera: Nuevo mensaje de contacto',
                f'De {name} <{email}>\n\nEscribio:\n\n{content}',
                'no-contestar@inbox.mailtrap.io',
                ['fco_jvr_33@live.com.mx'],
                reply_to=[email]
            )

            try:
                email.send()
                # Todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact') + '?ok')
            except:
                # algo no ha ido bien, redireccionamos a fail
                return redirect(reverse('contact') + '?fail')

    return render(request, "contact/contact.html", {'form':contact_form})
