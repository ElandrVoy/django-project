from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=40)
    surname = models.CharField(max_length=20)

    def __str__(self):
        """some sting for the future events"""
        return self.name