from django.db import models

class resume(models.Model):
    schooling=models.CharField(max_length=50)
    schooling_date=models.IntegerField()
    schooling_experiences=models.TextField(default="Experience in highschool")
    post=models.CharField(default="Experience in Graduation",max_length=50)
    TimeLapse=models.IntegerField()
    Experience=models.TextField(default="Experience in workingcompany")


# Create your models here.
