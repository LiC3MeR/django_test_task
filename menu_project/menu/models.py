from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)  # Статический URL
    url_name = models.CharField(max_length=255, blank=True, null=True)  # Именованный URL
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')

    def get_url(self):
        if self.url_name:
            try:
                return reverse(self.url_name)
            except:
                return self.url
        return self.url if self.url else '#'

    def __str__(self):
        return self.title