from django.db import models


class Project(models.Model):
    """ Model to represent any project """
    job_no = models.AutoField(primary_key=True)
    po_code = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    po_date = models.DateField()
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

    drawing = models.CharField(max_length=256, default="", blank=True, null=True)
    supplier_identification_no = models.TextField(default="", blank=True, null=True)
    revision = models.CharField(max_length=32, default="A")
    comment = models.CharField(max_length=256, default="", blank=True, null=True)

    quantity = models.IntegerField(default=0)
    uom = models.CharField(max_length=256, default="P")
    bbu_value = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    creation_timestamp = models.DateTimeField(auto_now_add=True)
    modified_timestamp = models.DateTimeField(auto_now=True)
    forecast_date = models.DateField(auto_now_add=True)

    project = models.ForeignKey('Project', on_delete=models.CASCADE)
