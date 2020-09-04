from django.urls import path
from .views import Index, load_district

urlpatterns = [
    path('', Index, name='index'),
    path('load-district', load_district, name='load-district'),
]