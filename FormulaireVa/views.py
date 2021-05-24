from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def formva(request):
    return render(request,'FormulaireVa/formulaireva.html')