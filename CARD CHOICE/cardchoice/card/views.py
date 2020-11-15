from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'card/index.html')
    
def new(request):
    return render(request, 'card/new.html')

def compare1(request):
    return render(request, 'card/compare1.html')

def compare2(request):
    return render(request, 'card/compare2.html')