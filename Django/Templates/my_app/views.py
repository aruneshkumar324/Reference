from django.shortcuts import render


def home(request):
    return render(request, 'my_app/index.html')


def variable_view(request):

    data = {
        'first_name': 'Arunesh',
        'last_name': 'kumar',
        'age': 23,
        'friends': ['Mohan', 'Dohan', 'Sohan', 'Pohan'],
        'num': [1,2,3,4,5,6],
        'student': {'name': 'Salman Khan', 'USN': '1EP16CS019'},
        'user_logged_in': True,
    }

    return render(request, 'my_app/variables.html', context=data)



def example_view(request):
    return render(request, 'my_app/example.html')