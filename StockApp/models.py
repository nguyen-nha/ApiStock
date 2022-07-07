from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=40)
    roe = models.DecimalField(max_digits=4, decimal_places=2)
    pb = models.DecimalField(max_digits=4, decimal_places=2)
    company = models.TextField()

    def __str__(self):
        return self.name