from django.shortcuts import render, redirect
from .form import userForm, medication, specialist
from .models import userRegistration, doctor_information, Medicalinformation

def user(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('information')
    form = userForm
    return render(request, "medical/signup.html", {'form':form})

def information(request):

    if request.method == 'POST':
        form = medication(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('medical_records')
    form = medication()
    context = {'medic':medication}
    return render(request, 'medical/medical_info.html', context)

def doctors(request):
    if request.method == 'POST':
        form = specialist(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_medical')
    form = specialist()
    context = {'doctor':specialist}
    return render(request, 'medical/doctor.html', context)

def medical_records(request):
    medical_details = Medicalinformation.objects.all()
    context = {'medical_details':medical_details}
    return render(request, 'medical/medical_record.html', context)

def user_medical(request):
    user_details = Medicalinformation.objects.all()
    context = {'user_details': user_details}
    return render(request, 'medical/user_medical_records.html', context)

def corona(request):
    return render(request, 'medical/covid.html')

def mosquito(request):
    return render(request, 'medical/malaria.html')