from django import forms

class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.CharField()
    edad = forms.IntegerField()

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    edad.widget.attrs['class'] = 'form-control'