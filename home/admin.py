from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("client_name",)


@admin.register(Contact)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Subscribe)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("email",)

