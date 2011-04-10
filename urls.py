from os import path as os_path
from django.conf import settings
from django.conf.urls.defaults import *
from FreeFoodColumbia.freefoodcolumbia.views import index
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^$',index),
    # Example:
    # (r'^FreeFoodColumbia/', include('FreeFoodColumbia.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve', kwargs={'document_root': os_path.join(settings.PROJECT_PATH, 'static')}),
)
