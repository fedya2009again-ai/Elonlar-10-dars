from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'price', 'created')
    list_filter = ('status',)
    inlines = [OrderProductInline]


admin.site.register(OrderProduct)
