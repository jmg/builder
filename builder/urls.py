from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT

from builder_app.views.main import *
from builder_app.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', IndexView.as_view()),    
    url(r'^about/$', AboutView.as_view()),
    url(r'^projects/$', ProjectListView.as_view()),
    url(r'^projects/create/$', ProjectCreateView.as_view()),
    url(r'^projects/follow/(?P<project_id>\d+)/$', ProjectFollowView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    #registration
    (r'^accounts/', include('registration.urls')),
    
    (r'^admin/', include(admin.site.urls)),
    
    #Static files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True}),
)

