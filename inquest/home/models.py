from django.db import models

# Create your models here.


class Questions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Answer lies in the Question')
    image = models.ImageField(blank=True, upload_to='questions/images')
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.title
