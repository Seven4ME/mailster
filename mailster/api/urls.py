from .views import *
from django.urls import path


urlpatterns = [
    path('pixel/<uuid>', PixelView.as_view())
]