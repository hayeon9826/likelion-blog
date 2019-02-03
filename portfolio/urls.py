from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.portfolio, name="portfolio"),
    url(r'^/download$', views.pdf_download, name='download'),
    url(r'^/new$', views.new_portfolio, name="new_portfolio"),
]