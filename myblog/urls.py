from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('<int:band_id>/', views.persons, name='persons'),
]