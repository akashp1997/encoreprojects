from django.db import models


class Project(models.Model):
    """ Model to represent any project """
    po_code = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    po_date = models.DateField()
    po_spec = models.CharField(max_length=256)
    supplier_name = models.CharField(max_length=256)

    addendum = models.IntegerField(default=0)
    modified_date = models.DateField(auto_now=True)
    revision = models.CharField(max_length=32, default="A")

    is_validated = models.BooleanField(default=False)


class BBURow(models.Model):
    """ Model to represent the BBU table's each row """
    po_line_item_no = models.IntegerField()
    po_position_no = models.IntegerField()

    erection_item = models.CharField(max_length=256)
    description = models.TextField()
    supplier_identification_no = models.TextField(null=True)
    uom = models.CharField(max_length=256)
    quantity = models.IntegerField(default=0)
    bbu_value = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    forecast_date = models.DateField(null=True)

    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    creation_timestamp = models.DateTimeField(auto_now_add=True)
