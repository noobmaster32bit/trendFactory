from django.contrib import admin
from Store.models import Category,Product,Size,OrderItems,Order
# Register your models here.

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(OrderItems)
admin.site.register(Order)


