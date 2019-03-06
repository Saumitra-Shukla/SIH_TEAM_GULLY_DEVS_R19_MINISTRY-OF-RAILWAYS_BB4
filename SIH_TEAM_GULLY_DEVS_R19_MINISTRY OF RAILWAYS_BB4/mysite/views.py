from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from newspapers.models import Preference,Newspaper_name,News
from django.core.mail import send_mail
from django.conf import settings

class TestPage(TemplateView):
    template_name = 'test.html'

def main(request):
	return render_to_response('main.html', {}, context_instance=RequestContext(request))

def email(request):

    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['abhi95103@gmail.com',]

    send_mail( subject, message, email_from, recipient_list )

    return redirect('redirect to a new page')
