from django.urls import path
from .views import getData,addShape

urlpatterns = [
    path('', getData, name='get_data'),
     path('add/', addShape, name='create_shape'),
]
