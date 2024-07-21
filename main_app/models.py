from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Category Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created By')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Product Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Value')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name='Category')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Created By')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name='Image')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

class StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_item', 
                                verbose_name='Product')
    
    barcode = models.CharField(max_length=100, unique=True, verbose_name='Barcode')
    manufacture_date = models.DateField(verbose_name='Manufacture Date')
    expiration_date = models.DateField(verbose_name='Expiration Date')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Created By")

    def __str__(self):
        return f'{self.product.name} - {self.barcode}'

    class Meta:
        verbose_name = "Stock Item"
        verbose_name_plural = "Stock Items"
        ordering = ['product', 'created_at']