from ejModelApp.forms import EmpleadoRegistroForm
from django.shortcuts import render
from ejModelApp.models import Empleado

""" Evitar la reinserción de datos al recargar la página """
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def empleadosData(request):
    empleados = Empleado.objects.all()
    data = {'empleados': empleados}
    return render(request, 'ejModelApp/empleados.html', data)

def empleadoRegistro(request):
    form = EmpleadoRegistroForm()
    
    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST)
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos
            Empleado.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                correo = form.cleaned_data['correo'],
                telefono = form.cleaned_data['telefono'],
                edad = form.cleaned_data['edad']
            )
            return HttpResponseRedirect(reverse('empleadosData'))
            
    data = {'form':form}  # Paso el formulario a la plantilla
    return render(request, 'ejModelApp/registroEmpleado.html',data)