from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def projects(request):
    return render(request, 'projects/projects.html')

@login_required
def project_list(request):
    # Your project view code
    pass

