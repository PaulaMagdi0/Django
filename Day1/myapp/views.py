from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')  # Render the home.html template

def dynamic_route(request, name):
    return HttpResponse(f"<h1>Welcome, {name}!</h1>")  # Displays the dynamic value