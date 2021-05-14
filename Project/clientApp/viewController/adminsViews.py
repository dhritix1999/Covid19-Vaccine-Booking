from django.shortcuts import render


#industry

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


#vaccine centers
def vaccine_centers_list(request):
    return render(request, 'admin/vaccine-center/vaccine-centers-table.html')


def add_vaccine_center(request):
    context = {"edit_industry": False}
    return render(request, 'admin/vaccine-center/add-edit-center.html')


def edit_vaccine_center(request):
    context = {"edit_industry": True}
    return render(request, 'admin/vaccine-center/add-edit-center.html')
