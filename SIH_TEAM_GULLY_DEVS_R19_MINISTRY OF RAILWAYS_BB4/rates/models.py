from django.conf import settings
from django.db import models
from django.utils import timezone
from newspapers.models import Newspaper_name,Preference

class News_rates(models.Model):
	newspaper_name=models.OneToOneField(Newspaper_name, on_delete=models.CASCADE)
	rate_text=models.TextField(null=True, blank=True)
	preferences=models.OneToOneField(Preference, on_delete=models.CASCADE)
class City(models.Model):
	city_text=models.TextField(null=True, blank=True)
