from django.db import models

class Homepage(models.Model):
    image=models.ImageField(upload_to='hpimages/')
    title=models.CharField(max_length=150)

    def __str__(self):
        return self.title