from django.db import models
from django.db import connection
class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"Image for {self.product.name}"



def my_view(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM my_table WHERE user_id = %s", [request.user.id])
    row = cursor.fetchone()
