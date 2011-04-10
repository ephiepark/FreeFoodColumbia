from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from freefoodcolumbia.models import Event

def index(request):
  name = 'freefoodColumbia App'
  event_list = Event.objects.all()
  t = get_template('trash.tmpl')
  html = t.render(Context({'event_list':event_list}))
  return HttpResponse(html)


# Create your views here.
