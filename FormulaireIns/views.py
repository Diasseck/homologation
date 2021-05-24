from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
#from .forms import CreerUtilisateur
from django.http import HttpResponse

# Create your views here.
def formacce(request):
    form=UserCreationForm(request.POST)
    context={'form':form}
    return render(request,'FormulaireIns/formulaireins.html',context)



