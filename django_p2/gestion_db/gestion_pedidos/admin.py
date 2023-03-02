from django.contrib import admin

# Importo los modelos de la app gestion_pedidos
from gestion_pedidos.models import Clientes, Articulos, Pedidos


class ClienteAdmin(admin.ModelAdmin):
    #Seteo que campos mostrar en el panel de administración
    list_display = ('nombre', 'direccion', 'email', 'telefono')
    #Estos son los paremetros que se pueden buscar en el panel de administración en la barra de búsqueda
    search_fields = ('nombre', 'telefono')

class ArticuloAdmin(admin.ModelAdmin):
    #Seteo que campos mostrar en el panel de administración
    list_display = ('nombre', 'seccion', 'precio')
    list_filter = ('seccion',) #Esto es para filtrar por sección
    
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'entregado')
    list_filter = ('fecha',) #Añade un panel para filtrar cierto rango de fechas
    date_hierarchy = 'fecha' #Esto es para filtrar por fecha, detecta los meses cargados 
    #en la base de datos y los muestra en el panel de administración para poder filtrar por fecha.

#Agrego el modelo al panel de administración 
admin.site.register(Clientes, ClienteAdmin)
admin.site.register(Articulos,ArticuloAdmin)
admin.site.register(Pedidos,PedidosAdmin)