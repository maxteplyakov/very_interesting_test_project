from django.db import models
from django.contrib.auth import get_user_model
from . import fields as map_fields

User = get_user_model()


class Memory(models.Model):
    place_name = models.CharField(max_length=200, verbose_name='Название места')
    text = models.TextField(verbose_name='Воспоминание')
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memories")
    address = map_fields.AddressField(max_length=200, blank=False, null=True, verbose_name='Адрес')
    geolocation = map_fields.GeoLocationField(max_length=100, blank=False, null=True, verbose_name='')
    img_url = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.place_name
