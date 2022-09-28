from django.contrib import admin
from resident.models import City, State, Buildings
# Register your models here.

admin.site.register(State)
admin.site.register(City)
admin.site.register(Buildings)