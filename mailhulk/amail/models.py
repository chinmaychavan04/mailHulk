from django.db import models
from django.utils.translation import activate

# Create your models here.
class Mail(models.Model):
    event = models.CharField(max_length=100)
    email = models.FileField(upload_to="excel")
    activated = models.BooleanField(default=False)

    def __str__(self) :
        return f"file id {self.id}"