from api import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('info/', views.InfoObject.as_view(), name='info'),
]

urlpatterns = format_suffix_patterns(urlpatterns)