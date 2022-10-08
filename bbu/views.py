from django.shortcuts import render, redirect

from .forms import ProjectForm
from .models import Project


def index(request):
    """ View to render the projects listing page """
    return render(request, 'index.html')


def create_project(request):
    """ View to render the create project form """
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)

        if project_form.is_valid():
            try:
                project = Project(**project_form.cleaned_data)
                project.save()
            except Exception as exp:
                project_form.errors['DBError'] = exp
            return redirect('homepage')

    else:
        project_form = ProjectForm()

    return render(request, 'create-project.html', {'form': project_form})
