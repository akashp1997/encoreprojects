from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Project, BBURow
from .serializers import ProjectSerializer, BbuItemSerializer


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
