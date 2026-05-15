from django.shortcuts import render
from portfolio.models import Portfolio

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    projects = Portfolio.objects.all()

    return render(request, 'portfolio.html', {
        'projects': projects
    })

def contact(request):
    return render(request, 'contact.html')
