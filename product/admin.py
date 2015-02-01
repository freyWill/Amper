from django.contrib import admin
from .models import Product, Category, ExtraImage
# Register your models here.

class ImageInline(admin.TabularInline):
	model = ExtraImage

class ProductAdmin(admin.ModelAdmin):
	Meta = Product
	list_display = ("pk","display_image","title","rating", "purchased", "viewed")
	prepopulated_fields = {'slug' : ('title',)}
	inlines = [
		ImageInline,
	]

class ExtraImageAdmin(admin.ModelAdmin):
	Meta = ExtraImage
	list_display = ('title', 'display_image', 'product')

class CategoryAdmin(admin.ModelAdmin):

	Meta = Category
	prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ExtraImage, ExtraImageAdmin)
