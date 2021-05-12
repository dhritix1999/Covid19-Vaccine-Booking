from django.shortcuts import render


# Create your views here.

# index page
def index(request):
    return render(request, 'index.html')


def patient_register(request):
    return render(request, 'patient/register.html')


def patient_homepage(request):
    return render(request, 'patient/homepage.html')


# ================================
def admin_homepage(request):
    return render(request, 'admin/homepage.html')


def industry_list(request):
    return render(request, 'admin/industry/industry-priority-table.html')


def add_industry(request):
    context = {"edit_industry": False}
    return render(request, 'admin/industry/add-edit-industry.html', context)


def edit_industry(request, pk):
    context = {
        "edit_industry": True,
        "industryID": pk
    }
    return render(request, 'admin/industry/add-edit-industry.html', context)
