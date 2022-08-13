from django.db import models
from events.models import Event

# Create your models here.
class Participant(models.Model):
	PARTCIPANT_STATUS = (
			('blank', 'Blank'),
			('voted', 'Voted')
		)

	name = models.CharField("Name", max_length=225)
	email = models.CharField("Email", max_length=225)
	status = models.CharField("Status", max_length=10, choices=PARTCIPANT_STATUS)
	invitation_code = models.CharField("Invitation Code", max_length=225)
	related_event = models.ForeignKey(Event, on_delete=models.CASCADE)