from django.contrib import admin
from .models import Furniture, Supplier, Order, Employee


class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'exist', 'date_create')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'date_create')
    list_editable = ('price', 'exist')
    list_filter = ('exist',)


admin.site.register(Furniture, FurnitureAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'agent_firstname', 'agent_name', 'agent_patronymic', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'agent_firstname')
    list_editable = ('exist',)
    list_filter = ('exist',)


admin.site.register(Supplier, SupplierAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_create', 'date_finish', 'status', 'price', 'address_delivery')
    list_display_links = ('id',)
    search_fields = ('date_create', 'address_delivery')
    list_editable = ('date_finish', 'status')
    list_filter = ('status',)


admin.site.register(Order, OrderAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'patronymic', 'date_hired', 'position', 'exist')
    list_display_links = ('id',)
    search_fields = ('date_hired', 'name', 'patronymic')
    list_editable = ('position',)
    list_filter = ('exist',)


admin.site.register(Employee, EmployeeAdmin)

