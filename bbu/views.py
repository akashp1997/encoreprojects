import json
import dateutil.parser

from django.contrib.auth.decorators import login_required
# from django.core import serializers
from django.forms.forms import NON_FIELD_ERRORS
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .forms import ProjectForm, BBURowForm
from .models import Project, BBURow
from .serializers import ProjectSerializer, BbuItemSerializer


@login_required
@require_http_methods(['GET'])
def index(request):
    """ View to render the projects listing page """
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


@login_required
@require_http_methods(['GET', 'POST'])
def create_project(request):
    """ View to render the create project form """
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        project_form.full_clean()
        if project_form.is_valid():
            try:
                project = Project(**project_form.cleaned_data)
                project.save()
                return redirect('homepage')
            except Exception as exp:
                project_form._errors[NON_FIELD_ERRORS] = project_form.error_class([str(exp)])
    else:
        project_form = ProjectForm()

    return render(request, 'create-project.html', {'form': project_form})


@login_required
@require_http_methods(['GET', 'POST'])
def view_efu(request, job_no):
    """ View to show the EFU BBU list """
    form_load = False
    if request.method == 'POST':
        bbu_form = BBURowForm(request.POST)
        bbu_form.full_clean()
        if bbu_form.is_valid():
            try:
                bbu_row = BBURow(**bbu_form.cleaned_data)
                bbu_row.project_id = job_no
                bbu_row.save()
                return redirect('project-page', job_no)
            except Exception as exp:
                bbu_form._errors[NON_FIELD_ERRORS] = bbu_form.error_class([str(exp)])
        form_load = True
    else:
        bbu_form = BBURowForm()
    project = Project.objects.get(job_no=job_no)
    bbu_list = BBURow.objects.filter(project_id=job_no).all()

    return render(request, 'bbu-table.html', {
        'project': project,
        'bbu_list': bbu_list,
        'form': bbu_form,
        'form_load': form_load
    })


@login_required
@require_http_methods(['POST'])
def edit_item(request, job_no):
    """ View to edit the item by fetching form data """
    bbu_row = BBURow.objects.get(pk=request.POST['id'])
    if bbu_row.project_id != job_no:
        return HttpResponse(status=400)

    bbu_row.description = request.POST['description']

    bbu_row.drawing = request.POST['drawing']
    bbu_row.supplier_identification_no = request.POST['supplier_identification_no']
    bbu_row.revision = request.POST['revision']
    bbu_row.comment = request.POST['comment']

    bbu_row.quantity = request.POST['quantity']
    bbu_row.uom = request.POST['uom']
    bbu_row.bbu_value = request.POST['bbu_value']

    bbu_row.full_clean()
    bbu_row.save()

    return redirect('project-page', job_no)


@login_required
@require_http_methods(['DELETE'])
def delete_bbu_row(request, job_no):
    delete_items = json.loads(request.body)
    BBURow.objects.filter(pk__in=[delete_item['id'] for delete_item in delete_items]).filter(project_id=job_no).delete()
    return HttpResponse(status=200)


class ProjectsViewSet(viewsets.ModelViewSet):
    """ View set for projects model """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def efu(self, request, pk=None):
        """ List all BBU items for a project """
        project = self.get_object()

        bbu_list_db = BBURow.objects.filter(project_id=project.job_no).all()
        bbu_list = BbuItemSerializer(data=bbu_list_db, many=True)
        bbu_list.is_valid()

        return Response(bbu_list.data)

    @efu.mapping.post
    def import_efu(self, request, pk=None):
        """ Import multiple BBU items for a project """
        project = self.get_object()
        bbu_list = BbuItemSerializer(data=request.data, many=True)
        bbu_list.is_valid(raise_exception=True)

        bbu_list.save()
        return HttpResponse(status=200)

    @efu.mapping.delete
    def delete_efu(self, request, pk=None):
        """ Import multiple BBU items for a project """
        project = self.get_object()
        print(request.data)
        BBURow.objects.filter(project=project.job_no).filter(id__in=request.data).delete()
        return HttpResponse(status=200)


class BbuViewSet(viewsets.ModelViewSet):
    """ View set for BBU entries model """
    queryset = BBURow.objects.all()
    serializer_class = BbuItemSerializer
