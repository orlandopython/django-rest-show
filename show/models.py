from django.db import models

class Show(models.Model):

    name = models.CharField(max_length=128)
    network = models.CharField(max_length=128)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name