from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    #changed for exercise 4
    path('index/', views.index, name = 'index'),
    path('about/', views.about, name ='about')

]