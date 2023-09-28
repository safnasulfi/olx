from django.db import models

# Create your models here.

class VehicleModels(models.Model):
    name=models.CharField(max_length=200)
    model_name=models.CharField(max_length=200)
    km_driven=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    contact=models.CharField(max_length=15)
    Image=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.name