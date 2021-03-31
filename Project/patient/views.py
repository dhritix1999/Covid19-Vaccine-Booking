from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return render(request, 'register.html')
