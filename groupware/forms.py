import datetime
from django import forms
from django.db.models import Q
from . import models
from django.contrib import messages


class TravelInsertForm(forms.ModelForm):
    class Meta:
        model = models.Travel
        fields = (
            "user",
            "type",
            "start_date",
            "end_date",
            "location_1",
            "address_1",
            "km_1",
            "reback_1",
            "location_2",
            "address_2",
            "km_2",
            "reback_2",
            "location_3",
            "address_3",
            "km_3",
            "reback_3",
            "location_4",
            "address_4",
            "km_4",
            "reback_4",
            "location_5",
            "address_5",
            "km_5",
            "reback_5",
            "why",
            "witness",
            "travel_pay",
            "traffice_pay",
            "sleep_pay",
            "eatandother_pay",
            "eatandother_comment",
        )

class TravelReportForm(forms.ModelForm):
    class Meta:
        model = models.Travel_report
        fields = (
            "travel",
            "oil_pay",
            "hipass_pay",
            "sleep_pay",
            "sleep_comment",
            "comment",
        )
    
    