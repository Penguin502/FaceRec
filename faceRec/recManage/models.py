from django.db import models

class peInfo(models.Model):
    peName = models.CharField(max_length=20)
    idNum  = models.CharField(max_length=17)
    sex    = models.CharField(max_length=4)
    pict   = models.TextField()
    feapict= models.TextField()



# Create your models here.
