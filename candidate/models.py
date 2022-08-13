from django.db import models
from events.models import Event

# Create your models here.
class Candidate(models.Model):

	name = models.CharField("Canidate's Name", max_length=255)
	vision = models.TextField(verbose_name="Candidate's Vision")
	mission = models.TextField(verbose_name="Candidate's Mission")
	score = models.IntegerField(verbose_name="Score")
	related_event = models.ForeignKey(Event, on_delete=models.CASCADE)



