from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.template.loader import get_template
from gestion_pedidos.models import Articulos

# Create your views here.

def formulario_busqueda(request):
    context = {'css_file':"search_bar.css"}
    # template = get_template("form.html")
    
    return render(request, "./form.html",context)

def busqueda(request):
    # print(request.GET['producto'])
    if  request.GET['producto']:
        # resultado = 'Articulos buscados: %r' % request.GET['producto']
        producto =  request.GET['producto']
        
        if len(producto) > 20:
            mensaje = 'Demasiado largo'
        
        else:
            #Busca en la base de datos si el termino buscado se encuentra en el campo nombre
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            
            return render(request, "./busqueda.html", {"articulos": articulos, "query": producto})
    
    else:
        mensaje = 'Terminos de búsqueda invalidos'
    return HttpResponse(mensaje)
   
   
def contacto(request):
    context = {'css_file':"./contacto.css"}
    
    if request.method == "POST":
        subject = request.POST['asunto']
        message = request.POST['mensaje'] + " " + request.POST['email']
        email_from = settings.EMAIL_HOST_USER
        recipiente_list = ['jackotes12@gmail.com']
        
        send_mail(subject, message, email_from, recipiente_list)
        
        messages.success(request, '¡Mensaje enviado con éxito!')
    # else:
    #     messages.warning(request, 'Por favor completa el formulario antes de enviarlo.')
    return render(request, "./contacto.html", context)
    