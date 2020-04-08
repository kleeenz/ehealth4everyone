from django.db import models
from django import forms


class userRegistration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)



class Medicalinformation(models.Model):

    Name = models.CharField(max_length=100)
    Age =  models.IntegerField()
    gender_choice = (('male','male'),
                     ('female','female'))
    Gender = models.CharField(max_length=10, choices=gender_choice, default='male')
    Travel_history = models.TextField(max_length=200)
    medical_history = models.TextField()


class doctor_information(models.Model):
    Doctor_name = models.CharField(max_length=100)
    occupation_type = (('professional', 'professional'),
                       ('traditional', 'traditional'))
    activity_sector = (('medicine', 'medicine'),
                       ('diagnosis', 'diagnosis'),
                       ('test', 'test'),
                       ('treatment', 'treatment'))
    specialist_info = (('dematologist', 'dematologist'),
                       ('neurologist', 'neurologist'),
                       ('surgeon', 'surgeon'),
                       ('paediatrician', 'paediatrician'))
    occupation_type_info = models.CharField(max_length=40, choices=occupation_type, default='professional')
    activity_sector_info = models.CharField(max_length=40, choices=activity_sector, default='test')
    specialization_area = models.CharField(max_length=50, choices=specialist_info, default='paediatrician')

