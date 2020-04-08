from . import views
from django.urls import path

urlpatterns = [
    path('', views.user, name = 'user'),
    path('information/', views.information, name = 'information'),
    path('doctors/', views.doctors, name = 'doctors'),
    path('medical_records', views.medical_records, name = 'medical_records'),
    path('user_medical', views.user_medical, name = 'user_medical'),
    path('corona/', views.corona, name = 'corona'),
    path('mosquito/', views.mosquito, name = 'mosquito')

]