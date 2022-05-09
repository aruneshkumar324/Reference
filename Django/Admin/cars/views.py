from django.shortcuts import render, redirect
from .models import Car


def list(request):
    cars = Car.objects.all()
    context = {
        "cars":cars,
    }
    return render(request, 'cars/list.html', context=context)


def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])

        Car.objects.create(brand=brand, year=year)

        return redirect('cars:list')

    return render(request, 'cars/add.html')


def delete_view(request, id):
    Car.objects.get(pk=id).delete()
    return redirect('cars:list')