# Create your views here.

from django.http import HttpResponse

from twilio.twiml import Response
from django_twilio.decorators import twilio_view


#@twilio_view
#def say(request, text, voice=None, language=None, loop=None):
#    """See: http://www.twilio.com/docs/api/twiml/say.
#    Usage::
#
#        # urls.py
#        urlpatterns = patterns('',
#            # ...
#            url(r'^say/$', 'django_twilio.views.say', {'text': 'hello, world!'})
#            # ...
#        )
#    """
#    r = Response()
#    r.say(text, voice=voice, language=language, loop=loop)
#    return r

def received_sms(request, text, voice=None, language=None, loop=None):
  r = Response()
  #r.say(text, voice=voice, language=language, loop=loop)
  #r.sms(text)
  r.sms('Polo!')
  return r

def hello_world(request):
  hello = 'Hello World'
  return HttpResponse(hello)
