from django.db import models

# Create your models here.
class Expense(models.Model):
    amount = models.IntegerField()
    data = models.DateField()
    vendor = models.TextField()
    icon = models.TextField()
    image = models.ImageField(upload_to="spendingapp/imagini/")
    category = models.TextField()



    def __str__(self):
        return f'[{self.amount}]:{self.data} - {self.vendor}'