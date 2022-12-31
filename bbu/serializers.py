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
    po_line_item_no = serializers.IntegerField()
    po_position_no = serializers.IntegerField()

    erection_item = serializers.CharField(max_length=256)
    description = serializers.CharField()

    drawing = serializers.CharField(required=False, default="", allow_null=True)
    supplier_identification_no = serializers.CharField(required=False, allow_null=True)
    revision = serializers.CharField(max_length=32, default="A", required=False, allow_null=True)
    comment = serializers.CharField(max_length=256, required=False, default="", allow_null=True)

    quantity = serializers.IntegerField(required=False, default=0, allow_null=True)
    uom = serializers.CharField(max_length=256, required=False, default="P", allow_null=True)
    bbu_value = serializers.DecimalField(decimal_places=2, max_digits=20, default=0, required=False, allow_null=True)

    forecast_date = serializers.DateField()
    class Meta:
        """ Metaclass definition for serializer """
        model = BBURow
        fields = '__all__'
        read_only_fields = ['creation_timestamp', 'modified_timestamp']

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, bbu_row, validated_data):
        """ Update the BBU entry """
        validated_data['drawing'] = validated_data.get('drawing', '')
        validated_data['comment'] = validated_data.get('comment', '')
        return super().update(bbu_row, validated_data)
