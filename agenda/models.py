from django.db import models


# Create your models here.
class Object(models.Model):
    from_time = models.TimeField()
    to_time = models.TimeField()
    name = models.CharField(max_length=100)
    by=models.ForeignKey('auth.User',on_delete=models.CASCADE)
