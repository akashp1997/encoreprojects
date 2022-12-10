from rest_framework import serializers

from .models import Project, BBURow


class ProjectSerializer(serializers.ModelSerializer):
    """ Define the API representation for projects """
    class Meta:
        """ Metaclass definition for serializer """
        model = Project
        fields = '__all__'
        read_only_fields = ['modified_date']

    def update(self, project, validated_data):
        """ Update the project details """
        project.name = validated_data.get('name', project.name)
        project.description = validated_data.get('description', project.description)
        project.po_date = validated_data.get('po_date', project.po_date)
        project.addendum = validated_data.get('addendum', project.addendum)
        project.revision = validated_data.get('revision', project.revision)
        project.is_validated = validated_data.get('is_validated', project.is_validated)

        project.save()
        return project


class BbuItemSerializer(serializers.ModelSerializer):
    """ Define the API representation for bbu items """
    class Meta:
        """ Metaclass definition for serializer """
        model = BBURow
        fields = '__all__'
        read_only_fields = ['creation_timestamp', 'modified_timestamp']

    def update(self, bbu_row, validated_data):
        """ Update the BBU entry """
        bbu_row.description = validated_data.get('description', bbu_row.description)
        bbu_row.drawing = validated_data.get('drawing', bbu_row.drawing)
        bbu_row.quantity = validated_data.get('quantity', bbu_row.quantity)
        bbu_row.uom = validated_data.get('uom', bbu_row.uom)
        bbu_row.supplier_identification_No = validated_data.get('supplier_identification_No', bbu_row.supplier_identification_No)
        bbu_row.revision = validated_data.get('revision', bbu_row.revision)
        bbu_row.comment = validated_data.get('comment', bbu_row.comment)
        bbu_row.bbu_value = validated_data.get('bbu_value', bbu_row.bbu_value)
