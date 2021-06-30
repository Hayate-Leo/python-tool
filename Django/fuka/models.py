from django.db import models
from django.urls import reverse

class Search(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True, blank=True)
    re_area = models.CharField(max_length=100, null=True, blank=True)
    re_rate = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_URL(self):
        return reverse('fuka-detail', kwargs={'pk:self.pk'})