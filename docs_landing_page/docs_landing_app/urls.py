from django.conf.urls import patterns, url

from docs_landing_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^logout/', views.user_logout, name='logout'),
)