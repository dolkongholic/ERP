import requests
import math
from django.shortcuts import render
from django.views.generic import View,DetailView
from . import forms, models
from groupware import models as groupware_models
from core import models as core_models
from users import models as users_models

# class Index_View(mixins.LoggedInOnlyView, View):
class Index_View(View):
    def get(self, request):
        return render(
            request,
            "core/index.html",
            {
                # "context": person_1_conunt,
            },
        )

# 작성 출장 신청서 디테일 뷰
class upper_travel_detail_View(DetailView):
    login_url = "users:login"
    def get_queryset(self):
        return groupware_models.Travel.objects.filter(pk=self.kwargs["pk"])

    template_name = "core/upper_travel_detail.html"
    context_object_name = "travel"

    def get_context_data(self, **kwargs):
        detail_model = groupware_models.Travel.objects.get(pk=self.kwargs["pk"])
        # 출장 날짜 계산
        span_day = (detail_model.end_date - detail_model.start_date).days
        #유류값 받아오기
        oil_money_list = core_models.oil_moneyModel.objects.all()
        oil_money=0
        for oil in oil_money_list:
            if str(detail_model.start_date)[0:10] == str(oil.date):
                oil_money = oil.oil_money
                break
            else :
                continue
        # 유류값 계산
        oil_km_money = float(detail_model.total_km) / float(detail_model.user.car_real_km) * float(oil_money)
        #총 금액 계산
        food_money = span_day * 3 * 8000
        sleep_money = span_day * 60000
        other_money = detail_model.eatandother_pay
        total_money = food_money + sleep_money + other_money + oil_km_money
        context = super(upper_travel_detail_View, self).get_context_data(**kwargs)
        context["span_day"] = span_day
        context["oil_money"] = oil_money
        context["oil_km_money"] = math.trunc(oil_km_money)
        context["total_money"] = math.trunc(round(total_money,-2))
        return context

# 출장  보고서 디테일 뷰
class upper_travel_report_detail_View(DetailView):
    login_url = "users:login"
    def get_queryset(self):
        return groupware_models.Travel.objects.filter(pk=self.kwargs["pk"])

    template_name = "core/upper_travel_report_detail.html"
    context_object_name = "travel"

    def get_context_data(self, **kwargs):
        detail_model = groupware_models.Travel.objects.get(pk=self.kwargs["pk"])
        report_detail_model = groupware_models.Travel_report.objects.get(travel_id=self.kwargs["pk"])
        # 출장 날짜 계산
        span_day = (detail_model.end_date - detail_model.start_date).days
        #유류값 받아오기
        oil_money_list = models.oil_moneyModel.objects.all()
        oil_money=0
        for oil in oil_money_list:
            if str(detail_model.start_date)[0:10] == str(oil.date):
                oil_money = oil.oil_money
                break
            else :
                continue
        # 유류값 계산
        oil_km_money = float(detail_model.total_km) / float(detail_model.user.car_real_km) * float(oil_money)
        #총 금액 계산
        food_money = span_day * 3 * 8000
        sleep_money = span_day * 60000
        other_money = detail_model.eatandother_pay
        total_money = food_money + sleep_money + other_money + oil_km_money
        # 차량 운행 기록 받아오기
        car_list = groupware_models.Travel_report_traffic.objects.filter(travel_report_id=report_detail_model.pk)
        # 숙박비 기록 받아오기
        sleep_list = groupware_models.Travel_report_sleep.objects.filter(travel_report_id=report_detail_model.pk)
        # 하이패스 기록 받아오기
        hipass_list = groupware_models.Travel_report_hipass.objects.filter(travel_report_id=report_detail_model.pk)        
        # 기타 사용 기록 받아오기
        other_list = groupware_models.Travel_report_other.objects.filter(travel_report_id=report_detail_model.pk)
        # 식대 사용 기록 받아오기
        food_list = groupware_models.Travel_report_food.objects.filter(travel_report_id=report_detail_model.pk)

        context = super(upper_travel_report_detail_View, self).get_context_data(**kwargs)

        context["span_day"] = span_day
        context["oil_money"] = oil_money
        context["oil_km_money"] = math.trunc(oil_km_money)
        context["total_money"] = math.trunc(round(total_money,-2))

        context["car_list"] = car_list
        context["sleep_list"] = sleep_list
        context["hipass_list"] = hipass_list
        context["other_list"] = other_list
        context["food_list"] = food_list

        context["span_day"] = span_day
        context["report_detail_model"] = report_detail_model

        return context

class upper_success_View(View):
    def get(self, request,pk,category):
        jarvis = models.jarvis_list.objects.filter(category=category).get(document_5=pk)
        acceptor = models.acceptor_list.objects.filter(jarvis_no_id=jarvis.id).get(acceptor_id=self.request.user.pk)
        if acceptor.priolity == 1 :
            acceptor.result = 0
            acceptor_tmp_1 = models.acceptor_list.objects.filter(jarvis_no_id=jarvis.id).get(priolity=2)
            acceptor_tmp_1.result = 0
            acceptor_tmp_1.save()
            acceptor_tmp_2 = models.acceptor_list.objects.filter(jarvis_no_id=jarvis.id).get(priolity=3)
            acceptor_tmp_2.result = 0
            acceptor_tmp_2.save()
        elif acceptor.priolity == 2 :
            acceptor.result = 1
            acceptor_tmp_1 = models.acceptor_list.objects.filter(jarvis_no_id=jarvis.id).get(priolity=1)
            acceptor_tmp_1.result = 1
            acceptor_tmp_1.save()
            acceptor_tmp_2 = models.acceptor_list.objects.filter(jarvis_no_id=jarvis.id).get(priolity=3)
            acceptor_tmp_2.result = 1
            acceptor_tmp_2.save()
        elif acceptor.priolity == 3 :
            acceptor.result = 2
            acceptor_tmp_1 = models.acceptor_list.objects.filter(jarvis_no_id=jarvis.id).get(priolity=1)
            acceptor_tmp_1.result = 2
            acceptor_tmp_1.save()
            acceptor_tmp_2 = models.acceptor_list.objects.filter(jarvis_no_id=jarvis.id).get(priolity=2)
            acceptor_tmp_2.result = 2
            acceptor_tmp_2.save()
        acceptor.save()

        #  최종 결제자 체크
        if len(models.acceptor_list.objects.filter(jarvis_no_id=jarvis.id).filter(result=0)) == 3:
            travel_data = groupware_models.Travel.objects.get(pk=self.kwargs["pk"])
            if(travel_data.status == 1):
                jarvis_data = models.jarvis_list.objects.filter(category=category).get(document_5=pk)
                jarvis_data.status = 1
                jarvis_data.save()
                travel_data.status = 2
                travel_data.save()
            else:    
                travel_data.status = 1
                travel_data.save()
            

        return render(
            request,
            "core/upper_success.html",
            {
                # "context": person_1_conunt,
            },
        )


class upper_fail_View(View):
    def get(self, request):
        return render(
            request,
            "core/upper_fail.html",
            {
                # "context": person_1_conunt,
            },
        )
