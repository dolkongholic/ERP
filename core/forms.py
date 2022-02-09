import datetime
from django import forms
from django.db.models import Q
from . import models
from django.contrib import messages


class JarvisInsertForm(forms.ModelForm):
    class Meta:
        model = models.jarvis_list
        fields = (
            "document_1",
            "document_2",
            "document_3",
            "document_4",
            "document_5",
            "document_6",
            "document_7",
            "document_8",
            "document_9",
            "status",
        )

class AcceptorInsertForm(forms.ModelForm):
    class Meta:
        model = models.acceptor_list
        fields = (
            "jarvis_no",
            "acceptor",
        )
    