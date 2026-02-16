from django.db import models

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

class Audio(models.Model):
    file = models.FileField(upload_to='audio/')

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

class Sandhya(models.Model):
    image = models.ImageField(upload_to='sandhya/')

class Aromal(models.Model):
    image = models.ImageField(upload_to='aromal/')