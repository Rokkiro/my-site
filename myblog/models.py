from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Persons(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + " from " + self.band.name

    

