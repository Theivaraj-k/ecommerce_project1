
from django.db import models
from django.utils.text import slugify





class Feature(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='features/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)
    processor = models.CharField(max_length=100, blank=True)
    ram = models.CharField(max_length=50, blank=True)
    graphics = models.CharField(max_length=100, blank=True)
    display = models.CharField(max_length=100, blank=True)
    storage = models.CharField(max_length=100, blank=True)
    connectivity = models.CharField(max_length=255, blank=True)
    battery = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    dimensions = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_color_list(self):
        return [color.color for color in self.colors.all()]
    
    def get_storage_list(self):
        return [storage.size for storage in self.storage_options.all()]


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.product.name} - {self.color}"


class ProductStorage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='storage_options')
    size = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.product.name} - {self.size}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.product.name}"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review for {self.product.name} by {self.name}"
    
    class Meta:
        ordering = ['-created_at']


class RelatedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='related_products')
    related = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='related_to')
    
    def __str__(self):
        return f"{self.product.name} - {self.related.name}"
    
    class Meta:
        unique_together = ('product', 'related')






#
# 
# 
#         

