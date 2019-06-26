from django.db import models

# Create your models here.

class Servicio(models.Model):
    name     = models.CharField(max_length=255, null=False)
    delete   = models.BooleanField(default = False)
    date_now = models.DateTimeField(default = False)
    class Meta:
        db_table = "servicio"