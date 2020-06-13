from django.contrib import admin
from core.models import Product, Rating
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating']
        
admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)