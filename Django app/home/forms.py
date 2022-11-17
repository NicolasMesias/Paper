from django import forms
from home.models import INFORMACION

#Modelform para crear con anterioridad un formulario
class INFORMACION_FORM(forms.ModelForm):
    class Meta:
        model = INFORMACION
        fields = [
            'nombre_imagen',
            'imagen',
            'upload_to',
            'callefinal',
            'resultado']
        labels = {
            'nombre_imagen': 'Nombre del archivo',
            'imagen': 'Imagen a subir',
            'upload_to': 'Fecha de subida',
            'callefinal': 'Dirección de la avería',
            'resultado': 'Resultado'}
        Widgets = {
            'nombre_imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.ImageField(), #Quizas se pueda mejorar
            'upload_to': forms.TextInput(attrs={'class': 'form-control'}),
            'callefinal': forms.TextInput(attrs={'class': 'form-control'}),
            'resultado': forms.TextInput(attrs={'class': 'form-control'})}