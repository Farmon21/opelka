import datetime

from django.db import models


class FormData(models.Model):
    customer = models.CharField(max_length=100)
    production_order = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    IDs = models.IntegerField()
    design = models.TextField()
    employee = models.CharField(max_length=100)
    tool = models.CharField(max_length=100)
    work_step = models.CharField(max_length=100)
    workplace = models.CharField(max_length=100)
    current_date = models.DateField()
    total_time = models.DurationField(default=datetime.timedelta(seconds=1))

    def __str__(self):
        return f"{self.customer} - {self.production_order}"

    class Meta:
        db_table = 'form_data'
