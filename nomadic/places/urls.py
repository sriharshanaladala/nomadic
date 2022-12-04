from django.urls import path
from . import views


urlpatterns = [
    path("places/", views.places, name="places"),
    path('place/<str:pk>', views.place, name="place"),
]
