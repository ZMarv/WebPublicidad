from django.shortcuts import render
from .models import *
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from django.shortcuts import redirect
import requests

def home(request):
    url = "http://worldtimeapi.org/api/timezone/America/Santiago"
    response = requests.get(url)
    data = response.json()
    return render(request, 'app/home.html',{'data': data})

def productos(request):
    suscripciones = Suscripcion.objects.all()
    suscripciones_con_paypal = []
    
    host = request.get_host()
    
    for suscripcion in suscripciones:
        paypal_checkout = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': suscripcion.precio_suscripcion,
            'item_name': suscripcion.nombre_suscripcion,
            'invoice': uuid.uuid4(),
            'currency_code': 'USD',
            'notify_url': f"http://{host}{reverse('paypal-ipn')}",
            'return_url': f"http://{host}{reverse('payment-success', kwargs={'id_suscripcion': suscripcion.id})}",
            'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'id_suscripcion': suscripcion.id})}",
        }

        paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
        
        suscripcion_con_paypal = {
            'suscripcion': suscripcion,
            'paypal': paypal_payment,
        }
        
        suscripciones_con_paypal.append(suscripcion_con_paypal)

    return render(request, 'app/productos.html', {"suscripciones_con_paypal": suscripciones_con_paypal})

def servicios(request):
    return render(request, 'app/servicios.html')


def PaymentSuccessful(request, id_suscripcion):
    product = Suscripcion.objects.get(id= id_suscripcion)
    return render(request, 'app/home.html', {'product': product})

def PaymentFailed(request, id_suscripcion):
    product = Suscripcion.objects.get(id= id_suscripcion)

    return render(request, 'app/home.html', {'product': product})

def banners(request):
    return render(request, 'app/banners.html')

def umbrella(request):
    return redirect('https://umbrellaclub.net')