from django import forms
from .models import Cliente, Pedido, Sucursal


class clienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']

class pedidoFormulario(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['tipo_cafe', 'unidades']
    #tipo_cafe = forms.CharField(max_length=30)
    #unidades = forms.IntegerField()

class sucursalFormulario(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['barrio', 'id_sucursal']
    #barrio = forms.CharField(max_length=30)
    #id_sucursal = forms.IntegerField()


