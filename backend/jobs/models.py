from django.db import models
from django.contrib.auth import get_user_model

class Job(models.Model):

    title           = models.CharField(max_length=30)
    date_created    = models.DateField(auto_now=True)
    level           = models.CharField(max_length=20)
    description     = models.CharField(max_length=200)
    experience      = models.PositiveIntegerField()

    poster = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Application(models.Model):

    applicant = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="applicant")
    job       = models.ForeignKey(Job,on_delete=models.CASCADE,related_name="job")

    date_applied = models.DateField(auto_now=True)
   
    def __str__(self):
       return f"user{self.applicant} applied to job {self.job}"
   