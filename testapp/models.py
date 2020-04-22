from django.db import models

# Create your models here.


class MyModel(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        unique_together = ("name", )
