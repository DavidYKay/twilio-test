from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

message = """
Hello, Los Angeles django users! I hope you are having a good time so far at
the meetup! Goodbye.
"""

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'pricing.views.received_sms', {'text': message}),
    #url(r'^$', 'django_twilio.views.say', {'text': message}),
    url(r'^$', 'django_twilio.views.sms', {'text': message}),

    # url(r'^hello_django/', include('hello_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
