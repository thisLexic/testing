from django.contrib import admin
from .models import Product, Branch, Entry, DailyCash
# Register your models here.
admin.site.register(Product)
admin.site.register(Branch)
admin.site.register(Entry)
admin.site.register(DailyCash)