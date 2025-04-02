from django.contrib import admin
from .models import Feature, Category, Product, ProductColor, ProductStorage, ProductImage, Review, RelatedProduct

# Register your models here.

admin.site.register(Feature)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(ProductStorage)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(RelatedProduct)

