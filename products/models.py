from ctypes import addressof
import email
import telnetlib
from tokenize import group
from django.db import models
from django.db.models.fields import BooleanField
from core import models as core_models

class Product(core_models.TimeStampedModel, models.Model):
    product_code = models.CharField(max_length=20, blank=True, null=True) # 물품명
    product_name_in = models.CharField(max_length=120, blank=True, null=True) # 물품명 내부
    product_name_out = models.CharField(max_length=120, blank=True, null=True) # 물품명 외부
    product_size = models.CharField(max_length=20, blank=True, null=True) # 물품 규격
    product_count= models.CharField(max_length=20, blank=True, null=True) # 물품 단위
    product_init_count = models.FloatField(blank=True, null=True) # 초기수량
    product_init_price_in = models.FloatField(blank=True, null=True) # 초기수량
    product_vat_in = BooleanField(default=False) # 입고단가 vat 포함여부
    product_init_price_out = models.FloatField(blank=True, null=True) # 초기수량
    product_vat_out = BooleanField(default=False) # 출고단가 vat 포함여부
    product_group = models.CharField(max_length=20, blank=True, null=True) # 물품 단위

    def __str__(self):
        return self.product_name_in


class Company(core_models.TimeStampedModel, models.Model):
    code = models.CharField(max_length=20, blank=True, null=True) # 코드
    name = models.CharField(max_length=100, blank=True, null=True) # 회사명
    owner = models.CharField(max_length=20, blank=True, null=True) # 대표자
    keyperson = models.CharField(max_length=20, blank=True, null=True) # 담당자
    type = models.CharField(max_length=20, blank=True, null=True) # 업태
    type_2 = models.CharField(max_length=20, blank=True, null=True) # 종목
    tel = models.CharField(max_length=20, blank=True, null=True) # 전화
    phone = models.CharField(max_length=20, blank=True, null=True) # 모바일
    email = models.CharField(max_length=20, blank=True, null=True) # 이메일
    address = models.CharField(max_length=20, blank=True, null=True) # 주소
    bank = models.CharField(max_length=20, blank=True, null=True) # 은행명
    bank_address = models.CharField(max_length=20, blank=True, null=True) # 계좌번호
    group = models.ForeignKey(
        "products.Company_group",
        related_name="comapny_group",
        on_delete=models.CASCADE) # 거래처 그룹

    def __str__(self):
        return self.name

class Company_group(core_models.TimeStampedModel, models.Model):
    name = models.CharField(max_length=100) # 그룹명

    def __str__(self):
        return self.name
