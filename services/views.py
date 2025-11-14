# services/views.py
from django.shortcuts import render

def services_view(request):
    # Your view logic here
    return render(request, 'services/services.html')