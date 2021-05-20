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


#medical issues
def medical_issues_list(request):
    return render(request, 'admin/medical-issues/medical-issue-eligibility-table.html')


def medical_add_medical_issue(request):
    context = {"edit_medical_issue": False}
    return render(request, 'admin/medical-issues/add-edit-eligibility-table.html', context)



def medical_edit_medical_issue(request):
    context = {
        "edit_medical_issue": True,
        "medicalIssueID": pk
    }
    return render(request, 'admin/medical-issues/add-edit-eligibility-table.html', context)

#vaccine centers
def vaccine_centers_list(request):
    return render(request, 'admin/vaccine-center/vaccine-centers-table.html')


def add_vaccine_center(request):
    context = {"edit_center": False}
    return render(request, 'admin/vaccine-center/add-edit-center.html', context)


def edit_vaccine_center(request, pk):
    context = {"edit_center": True,
               "vaccineCenterID": pk
               }
    return render(request, 'admin/vaccine-center/add-edit-center.html', context)

