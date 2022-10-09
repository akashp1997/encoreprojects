from django.shortcuts import render, redirect

from .forms import ProjectForm
from .models import Project, BBURow


def index(request):
    """ View to render the projects listing page """
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


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


def view_efu(request, po_code):
    """ View to show the EFU BBU list """
    project = Project.objects.get(po_code=po_code)
    bbu_list = BBURow.objects.filter(project_id=po_code).all()

    return render(request, 'bbu-table.html', {'project': project, 'bbu_list': bbu_list})
