from django.shortcuts import render
from .models import Patient


def office_view(request):
    all_patient = Patient.objects.all()
    context = {
        "patients":all_patient,
    }
    return render(request, 'office/index.html', context=context)