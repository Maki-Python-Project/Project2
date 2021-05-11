from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная страница',
        'values' : ['Some', 'kurwa perdole'],
        'obj' : {
            'car' : 'Mersedes',
            'age' : 18,
            'hobby' : 'workout'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')
