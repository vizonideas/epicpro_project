from django.conf.urls import patterns, include, url
from .views import HomeRegisterView,LoginView,DashboardView

urlpatterns = patterns('',

    url( r'^$', HomeRegisterView.as_view(), name='home' ),
    url( r'^dashboad/$', DashboardView.as_view(), name='dashboard' ),

    url(r'^login/$', 'django.contrib.auth.views.login', { 'template_name': 'projects/login.html' }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

)
