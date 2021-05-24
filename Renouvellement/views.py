from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pape1(request):
    return render(request,'Renouvellement/pape.html')
