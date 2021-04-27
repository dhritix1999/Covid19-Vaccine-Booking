from django.shortcuts import render


# Create your views here.

# index page
def index(request):
    return render(request, 'index.html')


def patient_register(request):
    return render(request, 'patient/register.html')


def admin_homepage(request):
    return render(request, 'admin/homepage.html')


def patient_homepage(request):
    return render(request, 'patient/homepage.html')
