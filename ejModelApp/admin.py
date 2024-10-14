from django.contrib import admin
""" Se agrega el modelo de Empleados """
from ejModelApp.models import Empleado

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','correo','telefono','edad')

admin.site.register(Empleado, EmpleadoAdmin)
