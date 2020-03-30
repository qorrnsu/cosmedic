from django.conf.urls import url
from . import handler

urlpatterns = [
    url(r'^search$', handler.search),
    url(r'^score$', handler.get_score),

]