from django.db import models

# Create your models here.

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50,verbose_name='Domicilio') # verbose_name para cambiar el nombre de la columna en el panel de administración
    email = models.EmailField(blank=True, null=True,verbose_name='Dirección email') #blank=True, null=True para que no sea obligatorio
    telefono = models.CharField(max_length=7)
    
    
    #En el AdminPanel, visualizo el nombre del cliente en reemplazo de object(1), object(2), etc.
    def __str__(self):
        return self.nombre
    


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    
    
    #En el AdminPanel, esto se ve reflejado al momento de ver los datos en la tabla.
    # def __str__(self):
    #     return 'El nombre: %s $%s ' % (self.nombre, self.precio)
    
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
