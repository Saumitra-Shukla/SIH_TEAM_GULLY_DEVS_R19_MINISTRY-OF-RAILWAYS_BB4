from django.contrib import admin
from .models import News,Newspaper_name,Preference

admin.site.register(News)
admin.site.register(Newspaper_name)
admin.site.register(Preference)