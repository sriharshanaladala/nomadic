
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def places(request):
    return HttpResponse("here are our best place to visit")

def place(request, pk):
    return HttpResponse("single place"+ '' + str(pk))


urlpatterns = [
    path('admin/', admin.site.urls),
    path("places/", places, name="places"),
    path('place/<str:pk>', place, name="place"),
]
