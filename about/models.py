from django.db import models

class About(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title