from django.urls import path
from . import views


urlpatterns = [
	path('', views.SpamMarker.as_view()),
    ]
