
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def places(request):
    return HttpResponse("here are our best place to visit")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("places/", places, name= "places"),
]
