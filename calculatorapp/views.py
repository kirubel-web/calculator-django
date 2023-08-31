from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    num1 = int(request.GET.get('number1'))
# Create your views here.
