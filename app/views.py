from django.shortcuts import render
from .models import *
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

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


def contacto(request):
    return render(request,'app/contacto.html')

def servicios(request):
    return render(request, 'app/servicios.html')


def CheckOut(request, id_suscripcion):
    product = Suscripcion.objects.get(id=id_suscripcion)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.precio_suscripcion,
        'item_name': product.nombre_suscripcion,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs={'id_suscripcion': product.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'id_suscripcion': product.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': product,
        'paypal': paypal_payment,
    }

    return render(request, 'app/checkout.html', context)


def PaymentSuccessful(request, id_suscripcion):
    product = Suscripcion.objects.get(id= id_suscripcion)

    return render(request, 'app/home.html', {'product': product})

def PaymentFailed(request, id_suscripcion):
    product = Suscripcion.objects.get(id= id_suscripcion)

    return render(request, 'app/home.html', {'product': product})