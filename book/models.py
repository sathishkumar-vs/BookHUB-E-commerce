from django.db import models
from django.conf import settings


class Category(models.Model):

    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):

    title = models.CharField(max_length=50,null=True)
    author = models.CharField(max_length=50,null=True)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
class CartItem(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.book.price

class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    @property
    def total_price(self):
        return sum(item.total_price() for item in self.orderitem_set.all())

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.book.price * self.quantity