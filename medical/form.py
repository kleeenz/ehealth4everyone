from django import forms
from.models import Medicalinformation, userRegistration, doctor_information


class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = userRegistration
        fields = ['username',
        'email',
        'password']



class medication(forms.ModelForm):
    class Meta:

        model = Medicalinformation

        fields = ['Name',
                  'Age',
                  'Gender',
                  'Travel_history',
                  'medical_history']

class specialist(forms.ModelForm):
    class Meta:
        model = doctor_information
        fields = '__all__'





