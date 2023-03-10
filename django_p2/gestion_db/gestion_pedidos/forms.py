from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    
#Para probarlo en el shell de python es:
    # - python manage.py shell
    # - from <nombre_projecto>.forms import <nombre_de_la_clase>
    # - <variable>=<nombre_de_la_clase>()
    # - print(<variable>)  --> si no indicamos nada, le da formato tabla al formulario creado
    # Para ver el formulario en otro formato que no sea tabla, se puede usar:
    # print(<variable>.as_<etiqueta_hmtl>())  
       # - print(<variable>.as_p())  --> da formato parrafo
       # - print(<variable>.as_ul())  --> da formato lista
       # - print(<variable>.as_table())  --> da formato tabla
       # - print(<variable>.as_div())  --> da formato div
       # - print(<variable>.as_text())  --> da formato texto...
    # <variable>.fields --> muestra los campos del formulario
    # <variable>.is_valid() --> devuelve True si el formulario es valido
    # <variable>.cleaned_data --> devuelve un diccionario con los datos del formulario
       
       