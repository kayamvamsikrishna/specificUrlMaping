from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def csk(request):
    return HttpResponse('Msd is the captain of csk')