from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
#from api import views
from rest_framework import routers
import api
import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns += [
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)