from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_medicament(request):
    return render(request,'Medicament/list_medicament.html')