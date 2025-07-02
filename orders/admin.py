from django.contrib import admin
from .models import Order,OrderProduct,Payment
# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    readonly_fields = ('payment','user','product','quantity','product_price','ordered')
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number','full_name','phone','email','order_total','tax','status','is_ordered']
    list_filter = ['status','is_ordered']
    search_fields = ['order_number','first_name','last_name','email']
    list_per_page = 10
    inlines = [OrderProductInline]
admin.site.register(Payment)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct)