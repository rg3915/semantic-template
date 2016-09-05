from django.conf.urls import url
from semantic.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
