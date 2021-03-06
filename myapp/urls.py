from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [

    url(r'^project', views.project, name = 'project'),
    url(r'^factors', views.factors, name = 'factors'),
    url(r'^datasource', views.datasource, name = 'datasource'), # November 7
    url(r'^$', views.index, name='index'),
    url(r'^plot/(?P<c>[A-Za-z ]+)/$', views.plot, name='plot'),
    url(r'^view_pic', views.view_pic, name='view_pic'),
    url(r'^view_map', views.view_map, name='view_map'),
    url(r'^change', views.change, name='change'),
]
