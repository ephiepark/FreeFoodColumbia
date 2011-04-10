from django.shortcuts import render_to_response
from django.template import RequestContext
from freefoodcolumbia.models import Event

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

def parseTime(strTime):
  indexColon = strTime.rfind(":")
  if indexColon != -1:
    if strTime[indexColon-2:indexColon-1].isdigit():
      hour = int(strTime[indexColon-2:indexColon])
    else:
      hour = int(strTime[indexColon-1:indexColon])
    minute = int(strTime[indexColon+1:indexColon+3])
  else:
    minute = 0
    hour = int(strTime[0:2])

  if strTime.rfind("pm") != -1 and strTime.rfind("am") == -1:
    hour += 12
  time = hour * 60 + minute
  return time
 
def parseDate(date_list):
  monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct","Nov","Dec"]
  dateD = int(date_list.date[5:7])
  numberMonth = 1;
  for nameMonth in monthName:
    if nameMonth == date_list.date[8:11]:
      month = numberMonth
    numberMonth = numberMonth + 1
  year = int(date_list.date[12:16])
  time = parseTime(date_list.date[20:27])
  return dateD*24*60 + month*24*60*30 + year*24*60*365 + time
  
  
# Create your views here.
