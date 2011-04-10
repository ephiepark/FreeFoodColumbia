import imaplib
import re
from datetime import datetime
from models import Event
M=imaplib.IMAP4_SSL('imap.gmail.com', 993)
M.login('freefoodcolumbia@gmail.com','falafelhack')
M.select()
typ, data = M.search(None, '(FROM "Facebook")')
for num in data[0].split():
	typ, data = M.fetch(num, '(RFC822)')
	location = re.search(r'Location:(.*)', data[0][1])
	if location: 
		place = location.group()
		print place
	match = re.search(r'Start Time:\s(.*)at\s(.*)', data[0][1])
	date = match.group(1)
	dayofweek = date[0:3];
	words = date.split();
	month = words[1][0:3]
	day = words[2]
	if len(day) == 1 : day="0"+day
	year = "2011"
	finaldate = dayofweek + "," + " " + month + " " + day + " " + year
	print finaldate
	time = match.group(2)
	print time
	title = re.search(r'Event:(.*)', data[0][1])
	if title: 
		desc = title.group()
		print desc
	more = re.search(r'To see more details, follow the link below:\n*([.\n]*)=3D=3D', data[0][1])
	if more: 
		moreinfo = more.group()
		print moreinfo
	#print data[0][1]
    #print 'Message %s\n%s\n' % (num, data[0][1])
    e = Event(date = entry.date + " at " + time, location = place, description = title.group())
	e.save()
M.close()
M.logout()

