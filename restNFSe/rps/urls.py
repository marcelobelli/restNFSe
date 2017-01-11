from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import RPSList, RPSDetail


urlpatterns = [
    url(r'^rps/$', RPSList.as_view()),
    url(r'^rps/(?P<pk>[0-9]+)/$', RPSDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
