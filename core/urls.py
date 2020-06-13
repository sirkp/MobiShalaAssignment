from django.conf.urls import url, include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from core.views import UserRegistrationApi, ProductListApi

app_name='api'

urlpatterns = [
    url(r'^register/$', UserRegistrationApi.as_view(), name='register'),
    url(r'^products/$', ProductListApi.as_view(), name='products'),
    path('login/', obtain_auth_token, name='login'),
]