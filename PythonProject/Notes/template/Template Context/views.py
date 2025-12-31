from django.http import  HttpResponse
from django.shortcuts import render


def home(request):

    num1 = 1
    num2 = 2
    num3 = 3
    sum = num1 + num2 + num3
    context = {'num1' : num1, 'num2' : num2, 'num3' : num3, 'sum' : sum}

    return render(request, 'home.html', context)


