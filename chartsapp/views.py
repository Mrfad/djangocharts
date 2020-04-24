from django.shortcuts import render
from .models import Country

def index(request):
    data = Country.objects.all()
    context = {'data':data}
    return render(request, 'chartsapp/index.html', context)
