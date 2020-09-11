from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.TextField()
    time = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    duration = models.IntegerField(default=0)
    ticket_price = models.IntegerField(default=0)
    tickets_available = models.IntegerField(default=0)

class Customer(models.Model):
    name = models.TextField()
    contact_no = models.CharField(max_length = 10, unique=True)

class Ticket(models.Model):
    movie_id = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    movie_name = models.TextField()
