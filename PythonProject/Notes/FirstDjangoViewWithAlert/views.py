from django.http import  HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("Hello World")
    # return HttpResponse(sum)
    return render(request, 'home.html')


