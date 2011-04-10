from freefoodcolumbia.models import Event
from django.contrib import admin

class FoodAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'source')

admin.site.register(Event, FoodAdmin)

