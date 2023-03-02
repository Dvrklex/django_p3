from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template.loader import get_template
from gestion_pedidos.models import Articulos
# Create your views here.

def formulario_busqueda(request):
    
    # template = get_template("form.html")
    
    return render(request, "./form.html")

def busqueda(request):
    # print(request.GET['producto'])
    if  request.GET['producto']:
        # resultado = 'Articulos buscados: %r' % request.GET['producto']
        producto =  request.GET['producto']
        
        #Busca en la base de datos si el termino buscado se encuentra en el campo nombre
        articulos = Articulos.objects.filter(nombre__icontains=producto)
        
        return render(request, "./busqueda.html", {"articulos": articulos, "query": producto})
    
    else:
        mensaje = 'Terminos de búsqueda invalidos'
    return HttpResponse(mensaje)
   
    