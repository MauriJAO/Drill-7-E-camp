from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.

@admin.register(Laboratorio)
class Laboratorioadmin(admin.ModelAdmin):
    list_display = ("id","nombre", "pais", "ciudad")


@admin.register(DirectorGeneral)
class DirectorGeneraladmin(admin.ModelAdmin):
    list_display = ("id","nombre","laboratorio", "especialidad")



@admin.register(Producto)
class Productoadmin(admin.ModelAdmin):
    list_display = ("nombre", "laboratorio", "f_fabricacion", "p_costo", "p_venta")