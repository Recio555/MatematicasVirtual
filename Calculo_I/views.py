from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'calculo/base.html')
    
    
    #return render(request, '')
    
    
    
def home(request):
    return render(request, 'calculo/home.html')