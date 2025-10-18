from django import forms
from .models import Marca, Moto, Cliente
from django.core.validators import MinValueValidator

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['marca', 'modelo', 'cilindrada', 'precio', 'año', 'estado', 'kilometros']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        numeric_fields = ['cilindrada', 'precio', 'año', 'kilometros']
        for field_name in numeric_fields:
            field = self.fields[field_name]
            field.validators.append(MinValueValidator(0))
            field.widget.attrs.update({'min': 0, 'step': 1})

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['marca'].queryset = Marca.objects.order_by('nombre')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class BuscarMotoForm(forms.Form):
    FILTROS = [
        ('marca', 'Marca'),
        ('modelo', 'Modelo'),
        ('cilindrada', 'Cilindrada'),
        ('año', 'Año'),
        ('estado', 'Estado'),
        ('kilometros', 'Kilómetros'),
    ]

    filtro = forms.ChoiceField(choices=FILTROS, required=True, label='Buscar por')
    query = forms.CharField(required=True, label='Término de búsqueda')
