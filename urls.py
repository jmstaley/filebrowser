from django.conf.urls.defaults import *

urlpatterns = patterns('filebrowser.views',
                       (r'browse/(?P<file_type>.*)/$', 'browse'),)
