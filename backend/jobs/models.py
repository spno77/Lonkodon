from django.db import models

class Job(models.Model):

    title           = models.CharField(max_length=30)
    date_created    = models.DateField(auto_now=True)
    level           = models.CharField(max_length=20)
    description     = models.CharField(max_length=200)
    experience      = models.PositiveIntegerField()


    def __str__(self):
        return self.title
    