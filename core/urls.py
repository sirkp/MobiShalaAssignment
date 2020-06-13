from django.conf.urls import url, include
from django.urls import path
from core.views import UserRegistrationApi
from rest_framework.authtoken.views import obtain_auth_token 

app_name='api'

urlpatterns = [
    url(r'^register/$', UserRegistrationApi.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]