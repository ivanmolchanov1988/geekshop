from django.contrib import admin

from mainapp.models import ProductCategory, Product

# Register your models here.

admin.site.register(ProductCategory)
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity', 'category'))
    readonly_fields = ('name',)
    ordering = ('-name',)
    search_fields = ('name', 'category__name')
