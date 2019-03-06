from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from newspapers.models import Preference,Newspaper_name,News


def main(request):
	
	return {
	'newspaper_name': Newspaper_name.objects.all().order_by('-id')
	}
