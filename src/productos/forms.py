from django.forms import Form, CharField, FloatField

# Formulario de busqueda

class FormularioBusqueda(Form):
     nombre_producto = CharField(max_length=150)


class FormularioAgregar(Form):

     nombre = CharField()
     marca =  CharField()
     precio  = FloatField()
