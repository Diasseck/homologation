"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Renouvellement.urls')),
    path('Medicament',include('Medicament.urls')),
    path('Composition',include('Composition.urls')),
    path('Formulairere', include('FormulaireRe.urls')),
    path('Formulaireen', include('FormulaireEn.urls')),
    path('Formulaireva', include('FormulaireVa.urls')),
    path('Formulairemo', include('FormulaireMo.urls')),
    path('Formulaireins', include('FormulaireIns.urls')),
    path('Formulaireacce', include('FormulaireAcce.urls')),

]
