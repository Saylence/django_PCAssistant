from django.urls import path
from .views import start_module


urlpatterns = [
    path('', start_module, name ='voice-help'),
]