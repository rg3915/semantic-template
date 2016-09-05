from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('semantic.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
]
