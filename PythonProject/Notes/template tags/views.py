from django.shortcuts import render
from datetime import datetime, timedelta


def home(request):

    name = "Nazim"
    city = "dhaka"
    country = "Bangladesh"
    age = 27
    skills = ["python", "Django", "FastAPI"]
    dob = datetime.now() - timedelta(days=30)
    button = "<button>Click</button>"
    isBangladeshi = True
    learners = [
        {'name' : 'Rahim'},
        {'name': 'Karim'},
        {'name': 'Rihan'},
        {'name': 'Rabbi'},
    ]
    isLogin = False

    products = [
        {"name": "Mango Box", "price": 1200},
        {"name": "Organic Honey", "price": 500},
        {"name": "Peanut Butter", "price": 400},
        {"name": "Brown Rice 5kg", "price": 550}
    ]

    context = {'name': name, 'city': city, 'country': country, 'age': age, 'skills': skills, 'dob': dob, 'button': button, 'isBangladeshi': isBangladeshi, 'learners': learners, 'isLogin': isLogin, 'products': products }
    return render(request, 'home.html', context)



