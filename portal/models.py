from django.db import models
from django.contrib.flatpages.models import FlatPage

class FlatPageAddon(models.Model):
    flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
    header = models.TextField(blank=True)
   
    def __str__(self):
        return "%s - %s" %(str(self.id), self.flatpage.title)

# Create your models here.
