from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.portfolio, name="portfolio"),
    url(r'^download$', views.pdf_download, name='download'),
    url(r'^new$', views.new_portfolio, name="new_portfolio"),
    url(r'^(?P<portfolio_id>\d+)/', views.portfolio_detail, name='portfolio_detail'),
    url(r'^(?P<pk>\d+)/remove/$', views.portfolio_remove, name="portfolio_remove")
]