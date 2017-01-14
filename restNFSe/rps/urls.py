from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import RPSList, RPSDetail


urlpatterns = [
    url(r'^$', RPSList.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', RPSDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
