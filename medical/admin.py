from django.contrib import admin
from .models import Medicalinformation, userRegistration, doctor_information

admin.site.register(userRegistration)
admin.site.register(Medicalinformation)
admin.site.register(doctor_information)