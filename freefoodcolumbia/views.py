from django.shortcuts import render_to_response
from django.template import RequestContext
from freefoodcolumbia.models import Event

def index(request):
  name = 'freefoodColumbia App' # whats this for?
  event_list = Event.objects.all()
  return render_to_response('trash.tmpl', {'event_list':event_list}, context_instance=RequestContext(request))


# Create your views here.
