from django.db import models

# Create your models here.


class MyModel(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        pass
        # unique_together = ("name", )
