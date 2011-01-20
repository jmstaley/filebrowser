from django.conf.urls.defaults import *

urlpatterns = patterns('imagebrowser.views',
                       (r'browse/(?P<file_type>.*)/$', 'browse'),)
