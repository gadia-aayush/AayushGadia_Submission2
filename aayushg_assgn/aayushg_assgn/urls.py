from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myauth/', include('myauth.urls')),
    path('spam/', include('spam.urls')),
    path('search/', include('search.urls')),

]
