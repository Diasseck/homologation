from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def formacce(request):
    return render(request,'Formulaireacce/formulaireacce.html')

