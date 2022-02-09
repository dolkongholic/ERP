
from django.db import models
from django.db.models.aggregates import Max
from core import models as core_models
from django.contrib.auth.models import AbstractUser


class User(core_models.TimeStampedModel, AbstractUser):
    user_number = models.CharField(max_length=20, blank=True, null=True) #사원번호
    name_en = models.CharField(max_length=120, blank=True, null=True) #영문 이름
    people_number = models.CharField(max_length=20, blank=True, null=True) #주민등록번호
    team_code = models.CharField(max_length=10, blank=True, null=True) #부서코드
    level = models.CharField(max_length=10, blank=True, null=True) #직급
    staff_level = models.IntegerField(default=99) #직급
    #0 = 대표이사, 1= 팀장, 2= 일반, 3 = 김수영대리
    phone = models.CharField(max_length=120, blank=True, null=True) # 모바일
    address = models.CharField(max_length=200, blank=True, null=True) #주소
    comment = models.CharField(max_length=200, blank=True, null=True) #적요
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True) #사진
    account_pic = models.ImageField(upload_to="account", blank=True, null=True) #통장사본
    people_card = models.ImageField(upload_to="people_card", blank=True, null=True) #주민등록증 사본
    poeple_papper = models.ImageField(upload_to="poeple_papper", blank=True, null=True) #등본 사본
    date_in = models.DateField(blank=True, null=True) #입사일
    date_type = models.CharField(max_length=20, blank=True, null=True) #입사구분
    date_out = models.DateField(blank=True, null=True) #퇴사일
    out_comment = models.CharField(max_length=200, blank=True, null=True) #퇴사사유
    bank = models.CharField(max_length=20, blank=True, null=True) #은행
    account = models.CharField(max_length=50, blank=True, null=True) #계좌번호
    account_ower = models.CharField(max_length=120, blank=True, null=True) #예금주
    graduation = models.CharField(max_length=120, blank=True, null=True) #학력사항
    cert = models.CharField(max_length=100, blank=True, null=True) #자격/면허
    language = models.CharField(max_length=100, blank=True, null=True) #외국어

    car_number = models.CharField(max_length=100, blank=True, null=True) #차량번호
    car_type = models.CharField(max_length=100, blank=True, null=True) #차종
    car_cc = models.CharField(max_length=100, blank=True, null=True) #배기량(cc)
    car_oil = models.CharField(max_length=100, blank=True, null=True) #연료의 종류
    car_auth_km = models.CharField(max_length=100, blank=True, null=True) #공인 연비
    car_real_km = models.CharField(max_length=100, blank=True, null=True) #실제 연비
    

    def __str__(self):
        return self.username

class VacationList(core_models.TimeStampedModel,models.Model):
    type = models.CharField(max_length=120)
    add_date = models.FloatField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    target_people = models.ManyToManyField(User)

    def __str__(self):
        return self.type

class VacationUse(core_models.TimeStampedModel,models.Model):
    type= models.ForeignKey(
        "users.VacationList",
        related_name="VacationList",
        on_delete=models.CASCADE)
    start_date = models.DateField()
    start_date_morning = models.BooleanField(default=True)
    start_date_afternoon = models.BooleanField(default=True)
    end_date = models.DateField()
    end_date_morning = models.BooleanField(default=True)
    end_date_afternoon = models.BooleanField(default=True)
    user = models.ForeignKey(
        "users.User",
        related_name="VacationList",
        on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=200)
    accepter_1= models.ForeignKey(
        "users.User",
        related_name="accepter_1",
        on_delete=models.CASCADE, blank=True, null=True)
    accepter_1_result = models.IntegerField(default=0)
    accepter_2= models.ForeignKey(
        "users.User",
        related_name="accepter_2",
        on_delete=models.CASCADE, blank=True, null=True)
    accepter_2_result = models.IntegerField(default=0)
    def __str__(self):
        return self.type.type

