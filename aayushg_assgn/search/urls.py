from django.urls import path
from . import views


urlpatterns = [

    path("<str:ip>/", views.Search.as_view()),
    ]