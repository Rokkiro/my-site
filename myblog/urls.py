from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('<int:band_id>/', views.persons, name='persons'),
]