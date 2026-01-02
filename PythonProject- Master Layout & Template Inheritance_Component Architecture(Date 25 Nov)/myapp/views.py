from django.shortcuts import render
from datetime import datetime, timedelta


def home(request):

    return render(request, 'home.html')



