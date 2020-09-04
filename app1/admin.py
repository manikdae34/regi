from django.contrib import admin

from .models import Person, Division, District, Upazila

admin.site.register(Person)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)

