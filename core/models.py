from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    rating = models.FloatField(default=float(0))

    def __str__(self):
        return self.name
    

class Rating(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ratings')
    rating = models.FloatField()

    def save(self, *args, **kwargs):
        try:
            product = Product.objects.get(id=self.product.id)
            ratings_list = list(product.product_ratings.all().values_list('rating', flat=True))
            product.save()
        except Exception as e:
            raise e    
        super().save(*args, **kwargs)