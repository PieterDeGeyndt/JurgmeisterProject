from django.db import models
from django.db.models.fields import TextField

class Cocktails(models.Model):
    title = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='cocktails/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]