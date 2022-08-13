from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):

	name = models.CharField("Name", max_length=225)
	start_date = models.DateField("Start Date")
	end_date = models.DateField("End Date")
	creator = models.ForeignKey(User, on_delete=models.CASCADE)

