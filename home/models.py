from django.db import models


doc_type_choices =  [
    ('1','Notesheet'),
    ('2','File'),
    ('3','Letter Pad'),
    ('4','Plain Application'),
    ('5','Form/Leave Application'),
    ('6','Others'),
]

internal_from_choices = [
    ('1','Department'),
    ('2','Section'),
    ('3','Centre'),
    ('4','Others'),
]

external_from_choices = [
 ('1','MHRD'),
 ('2','PMO'),
 ('3','NHPC'),
]

class internal_letter(models.Model):
    si_no       = models.IntegerField()
    in_date     = models.DateField()
    doc_type    = models.CharField(max_length=1,choices=doc_type_choices)
    reference   = models.CharField(max_length=50)
    fromm       = models.CharField(max_length=1,choices=internal_from_choices)
    out_date    = models.DateField()
    to          = models.CharField(max_length=1,choices=internal_from_choices)
    subject     = models.CharField(max_length=50)
    remarks     = models.CharField(max_length=500)

class external_letter(models.Model):
    si_no           = models.IntegerField()
    receipt_date    = models.DateField()
    fromm           = models.CharField(max_length=1,choices=external_from_choices)
    subject         = models.CharField(max_length=50)
    marked_to       = models.CharField(max_length=100)
    action_needed   = models.CharField(max_length=300)
    file            = models.CharField(max_length=100)
    remarks         = models.CharField(max_length=500)
