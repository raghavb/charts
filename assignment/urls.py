from django.conf.urls import patterns, url
from django.conf import settings

#Django URL displatcher. Helps to route the application.
urlpatterns = patterns('',
url(r'^$', 'assignment.views.displayCharts', name='home'), 
url(r'^about$', 'assignment.views.about', name='about'), 
url(r'^charts/(.*)$', 'assignment.views.displayCharts'),
url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'assignment/login_page.html'}, name = 'login'),
url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
url(r'^register$', 'assignment.views.register', name='register'),
url(r'^search$', 'assignment.views.search', name='search'),
url(r'^upload$', 'assignment.views.upload', name='upload'),
url(r'^.*', 'assignment.views.raise404', name='404'),
)

if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns() 
