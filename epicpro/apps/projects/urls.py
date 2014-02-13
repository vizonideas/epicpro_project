from django.conf.urls import patterns, include, url
from .views import HomeRegisterView,LoginView,DashboardView,TeamHomeView,ProjectsHomeView,ResumeHomeView,TeamUpdateView

urlpatterns = patterns('',

    url( r'^$', HomeRegisterView.as_view(), name='home' ),
    url( r'^dashboad/$', DashboardView.as_view(), name='dashboard' ),
    url( r'^team/$', TeamHomeView.as_view(), name='team' ),
    url( r'^projects/$', ProjectsHomeView.as_view(), name='projects' ),
    url( r'^resume/$', ResumeHomeView.as_view(), name='resume' ),

    url( r'^team/(?P<pk>\d+)$/', TeamUpdateView.as_view(), name='update_team' ),

    url(r'^login/$', 'django.contrib.auth.views.login', { 'template_name': 'projects/login.html' }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

)
