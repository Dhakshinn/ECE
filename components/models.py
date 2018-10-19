from django.db import models

# Create your models here.
class component(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=100)
    total_quantity=models.IntegerField()
    available_quantity=models.IntegerField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return  self.name

    def clean(self):
        self.name=self.name.upper()