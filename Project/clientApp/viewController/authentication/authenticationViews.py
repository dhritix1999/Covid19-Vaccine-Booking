from django.shortcuts import render


# Create your views here.

# index page
def index(request):
    return render(request, 'index.html')


def patient_register(request):
    return render(request, 'authentication/patient-register.html')
