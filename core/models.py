from pyexpat import model
from xml.dom.xmlbuilder import DocumentLS
from django.db import models
from core import models as core_models

class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class jarvis_list(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.IntegerField()
    document_title = models.CharField(max_length=100, null=True,blank=True)
    document_user = models.CharField(max_length=100, null=True,blank=True)
    document_1 = models.IntegerField(default=0)
    document_2 = models.IntegerField(default=0)
    document_3 = models.IntegerField(default=0)
    document_4 = models.IntegerField(default=0)
    document_5 = models.IntegerField(default=0)
    document_6 = models.IntegerField(default=0)
    document_7 = models.IntegerField(default=0)
    document_8 = models.IntegerField(default=0)
    document_9 = models.IntegerField(default=0)
    status = models.IntegerField()

    def __str__(self):
        return self.document_title

class acceptor_list(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    jarvis_no = models.ForeignKey(
        "core.jarvis_list",
        related_name="jarvis_list_no",
        on_delete=models.CASCADE)
    acceptor = models.ForeignKey(
        "users.User",
        related_name="accpetor_list_user",
        on_delete=models.CASCADE
    )
    priolity = models.IntegerField()
    result = models.IntegerField(default=0)

    def __str__(self):
        return self.acceptor.username
        
class oil_moneyModel(models.Model):
    date = models.DateField()
    oil_type = models.CharField(max_length=10)
    oil_money = models.FloatField()
    def __str__(self):
        return str(self.date)