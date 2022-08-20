from django.urls import path, include
from . import views

app_name = 'web_base'
urlpatterns = [
	path('', views.index_home, name='home'),
	path('web/', include('django.contrib.auth.urls')),
	path('web/register', views.sign_up, name='sign_up'),
]