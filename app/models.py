from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return f"Banner {self.id}"


class Audio(models.Model):
    file = models.FileField(upload_to='audio/')

    class Meta:
        verbose_name = "Audio File"
        verbose_name_plural = "Audio Files"

    def __str__(self):
        return f"Audio {self.id}"


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return f"Gallery Image {self.id}"


class Sandhya(models.Model):
    image = models.ImageField(upload_to='sandhya/')

    class Meta:
        verbose_name = "Sandhya Image"
        verbose_name_plural = "Sandhya Images"

    def __str__(self):
        return f"Sandhya Image {self.id}"


class Aromal(models.Model):
    image = models.ImageField(upload_to='aromal/')

    class Meta:
        verbose_name = "Aromal Image"
        verbose_name_plural = "Aromal Images"

    def __str__(self):
        return f"Aromal Image {self.id}"
