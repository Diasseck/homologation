from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def formen(request):
    return render(request,'FormulaireEn/formulaireacce.html')