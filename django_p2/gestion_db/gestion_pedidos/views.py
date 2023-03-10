from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.template.loader import get_template
from gestion_pedidos.models import Articulos
from gestion_pedidos.forms import FormularioContacto
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
    context = {'css_file':"./contacto.css"} #Estilos para la pagina de contacto
    #Prueba utilizando formulario de Api Forms
    if request.method == 'POST':
        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():
            #Guardo la informacion del formulario en un diccionario
            info_formulario = miFormulario.cleaned_data
            send_mail(info_formulario['asunto'], 
                      info_formulario['mensaje'], 
                      info_formulario.get('email', ''), #<varaiable>.get(<clave>, <email_configurado_settings.py>)
                      ['ejemplo@gmail.com']
                      ) #Envia el correo
            messages.success(request, '¡Mensaje enviado con éxito!')
    else:
        miFormulario = FormularioContacto()
    
    return render(request,'formulario_contacto_apiform.html', {'form': miFormulario})
    
    #Primera prueba de envio de correo 
    # if request.method == "POST":
    #     subject = request.POST['asunto']
    #     message = request.POST['mensaje'] + " " + request.POST['email']
    #     email_from = settings.EMAIL_HOST_USER
    #     recipiente_list = ['ejemplo@gmail.com']
        
    #     send_mail(subject, message, email_from, recipiente_list)
        
    #     messages.success(request, '¡Mensaje enviado con éxito!')
    # # else:
    # #     messages.warning(request, 'Por favor completa el formulario antes de enviarlo.')
    # return render(request, "./contacto.html", context)
    