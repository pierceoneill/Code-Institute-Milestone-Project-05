from django.contrib import admin
from .models import Babysitter
from .models import Education
from .models import Work
from .models import Reference

class BabysitterAdmin(admin.ModelAdmin):
  list_display = ('id', 'firstName', 'lastName', 'email', 'phone')
  list_display_links = ('id', 'firstName', 'lastName')
  search_fields = ('firstName',)
  list_per_page = 25

# Register your models here.
admin.site.register(Babysitter, BabysitterAdmin)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Reference)