from django.shortcuts import render

def index(request):
    note = {'catalog': {'Pizza': 'a common stuff'}}
    return render(request, 'land.html', note)