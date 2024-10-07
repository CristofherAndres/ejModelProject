from django.shortcuts import render
from ejModelApp.models import Empleado


# Create your views here.
def empleadosData(request):
    empleados = Empleado.objects.all()
    data = {'empleados': empleados}
    return render(request, 'ejModelApp/empleados.html', data)