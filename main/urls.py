from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.main, name="main"),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^base/$', views.base, name='base'),
    url(r'^new/', views.new, name="new"),
    url(r'(?P<post_id>\d+)/remove/$', views.post_remove, name = "post_remove"),
]