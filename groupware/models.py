from re import L
from sys import flags
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Travel(models.Model):
    user = models.ForeignKey(
        "users.user",
        related_name="travel_user",
        on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location_1 = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=100)
    km_1 = models.FloatField(default=0)
    reback_1 = models.BooleanField(default=False)
    location_2 = models.CharField(max_length=20,null=True, blank=True)
    address_2 = models.CharField(max_length=100,null=True, blank=True)
    km_2 = models.FloatField(default=0,null=True, blank=True)
    reback_2 = models.BooleanField(default=False)
    location_3 = models.CharField(max_length=20,null=True, blank=True)
    address_3 = models.CharField(max_length=100,null=True, blank=True)
    km_3 = models.FloatField(default=0,null=True, blank=True)
    reback_3 = models.BooleanField(default=False)
    location_4 = models.CharField(max_length=20,null=True, blank=True)
    address_4 = models.CharField(max_length=100,null=True, blank=True)
    km_4 = models.FloatField(default=0,null=True, blank=True)
    reback_4 = models.BooleanField(default=False)
    location_5 = models.CharField(max_length=20,null=True, blank=True)
    address_5 = models.CharField(max_length=100,null=True, blank=True)
    km_5 = models.FloatField(default=0,null=True, blank=True)
    reback_5 = models.BooleanField(default=False)
    why = models.CharField(max_length=100)
    total_km = models.FloatField(default=0,null=True, blank=True)
    witness = models.CharField(max_length=100,null=True, blank=True)
    travel_pay = models.IntegerField(null=True, blank=True)
    traffice_pay = models.IntegerField(null=True, blank=True)
    sleep_pay = models.IntegerField(null=True, blank=True)
    eatandother_pay = models.IntegerField(null=True, blank=True)
    eatandother_comment = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.location_1

class Travel_report(models.Model):
    travel = models.ForeignKey(
        "groupware.Travel",
        related_name="travel_report_travel",
        on_delete=models.CASCADE)
    oil_pay = models.FloatField(blank=True, null=True)
    hipass_pay = models.IntegerField(blank=True, null=True)
    # 추가 사용한 숙박비
    sleep_pay = models.IntegerField(blank=True, null=True)
    sleep_comment = models.CharField(max_length=300, blank=True, null=True)
    other_pay = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.travel

class Travel_report_sleep(models.Model):
    travel_report = models.ForeignKey(
        "groupware.Travel_report",
        related_name="sleep_report",
        on_delete=models.CASCADE)
    img = models.ImageField(upload_to="travel/report/sleep/",blank=True, null=True) #사진
    date = models.DateField(blank=True, null=True)
    pay = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.travel

class Travel_report_traffic(models.Model):
    travel_report = models.ForeignKey(
        "groupware.Travel_report",
        related_name="traffic_report",
        on_delete=models.CASCADE)
    img = models.ImageField(upload_to="travel/report/traffic/",blank=True, null=True) #사진
    date = models.DateField(blank=True, null=True)
    km = models.FloatField(blank=True, null=True)
    start = models.CharField(max_length=50,blank=True, null=True)
    end = models.CharField(max_length=50,blank=True, null=True)
    oneway = models.BooleanField(default=False)
    def __str__(self):
        return self.travel

class Travel_report_other(models.Model):
    travel_report = models.ForeignKey(
        "groupware.Travel_report",
        related_name="other_report",
        on_delete=models.CASCADE)
    img = models.ImageField(upload_to="travel/report/other/",blank=True, null=True) #사진
    date = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=100,blank=True, null=True)
    pay = models.IntegerField(default=0,blank=True, null=True)
    def __str__(self):
        return self.travel

class Travel_report_hipass(models.Model):
    travel_report = models.ForeignKey(
        "groupware.Travel_report",
        related_name="hipass_report",
        on_delete=models.CASCADE)
    img = models.ImageField(upload_to="travel/report/hipass/",blank=True, null=True) #사진
    date = models.DateField(blank=True, null=True)
    start = models.CharField(max_length=50,blank=True, null=True)
    end = models.CharField(max_length=50,blank=True, null=True)
    pay = models.IntegerField(default=0,blank=True, null=True)
    def __str__(self):
        return self.travel
    
class Travel_report_food(models.Model):
    travel_report = models.ForeignKey(
        "groupware.Travel_report",
        related_name="food_report",
        on_delete=models.CASCADE)
    img = models.ImageField(upload_to="travel/report/food/",blank=True, null=True) #사진
    date = models.DateField(blank=True, null=True)
    pay = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.travel