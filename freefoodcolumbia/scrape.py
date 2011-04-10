import feedparser
from datetime import datetime
from models import Event
ColumbiaBuildings = ['Lerner', 'Butler', 'John Jay', 'Carmen', 'Hartley', 'Wallach',
            'Hamilton', 'Furnald', 'Mcbain', 'Broadway', 'Schapiro', 'Ruggles',
            'Hogan', 'Watt', 'EC', 'East Campus', 'Journalism', 'Kent', 'Dodge',
            'Philosophy', 'Maison Francaise', 'Buell', 'Lewisohn', 'Mathematics',
            'Math', 'Pupin', 'Northwest Corner', 'NoCo', 'Noco', 'Mudd', 'Schermerhorn',
            'Avery', 'Fayerweather', 'Havemeyer', 'Uris', 'Wein', 'Woodbridge', 'River',
            'Fitness Center', 'Low Plaza', 'Furnald Lawn', 'Teacher\'s College',
            'Low Library', 'SIPA', 'International Affairs', 'Law School', 'Casa Italiana',
            'Casa Hispanica', 'Earl', 'Barnard', 'Diana', 'Vag', 'Hewitt', 'Altschul',
            'Claremont', 'College Walk']
urltoscrape = 'http://bwog.com/feed/'
d = feedparser.parse(urltoscrape)
for entry in d.entries:
    for cat in entry.categories:
        if cat[1]=="free food":
            e = Event(date = entry.date, location = "Columbia", description = entry.title, source = entry.link);
            e.save()
            print entry.date
            print entry.title
            print entry.link
            print "\n"
