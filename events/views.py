from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def event_index(request):
	return render(request, 'events/event-dashboard.html')