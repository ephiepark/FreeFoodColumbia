from django.shortcuts import render_to_response
from django.template import RequestContext
from freefoodcolumbia.models import Event
import time
from datetime import datetime

def index(request):
#  name = 'freefoodColumbia App' # whats this for?
  
  event_list = Event.objects.all()
  event_list1 = []
  i=0
  for event in event_list:
    event_list1.append((parseDate(event),i))
    i=i+1
  event_list1.sort()
  event_list2 = []
  for e in event_list1:
    event_list2.append(event_list[e[1]])
  return render_to_response('trash.tmpl', {'event_list':event_list2}, context_instance=RequestContext(request))

def parseTime(year, month, dateD, strTime):
  strTime = strTime.lstrip()
  strTime = strTime.rstrip()
  
  indexColon = strTime.find(":")
  if indexColon != -1:
    if strTime[indexColon-2:indexColon-1].isdigit():
      hour = int(strTime[indexColon-2:indexColon])
    else:
      hour = int(strTime[indexColon-1:indexColon])
    minute = int(strTime[indexColon+1:indexColon+3])
  else:
    hour = int(strTime.split(" ", 1)[0])
    minute = 0

  if strTime.rfind("pm") != -1 and strTime.rfind("am") == -1:
    if hour == 12: 
      hour = 0
    hour += 12

  if strTime.rfind("pm") == -1 and strTime.rfind("am") == -1:
    if hour < 9:
      hour += 12
  
  return datetime(year, month, dateD, hour, minute)

def form(request):
  if 'datetime' in request.GET and request.GET['datetime']:
    e = Event(date = request.GET['datetime'], location = request.GET['location'], description = request.GET['description'], source = request.GET['source'])
    e.save()
  return render_to_response('form.tmpl')
  
def parseDate(date_list):
  temp = str(date_list.date[4:16]).lstrip()
  temp = temp.rstrip()
  year = time.strptime(temp,"%d %b %Y").tm_year
  month = time.strptime(temp,"%d %b %Y").tm_mon
  dateD = time.strptime(temp,"%d %b %Y").tm_mday
  time1 = parseTime(year,month,dateD,date_list.date[19:])
  return time1
  
  
# Create your views here.
