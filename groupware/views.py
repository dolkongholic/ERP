import requests
import math
import datetime
import requests
from unicodedata import category
from django.shortcuts import render, redirect
from django.views.generic import View,ListView,FormView,DetailView
from django.urls import reverse,reverse_lazy
from . import forms, models
from core import models as core_models
from users import models as users_models
from django.db.models import Q

# class Index_View(mixins.LoggedInOnlyView, View):
class upper_travel_list_View(ListView):
       
    def get(self, request):
        travel_list = models.Travel.objects.filter(user_id = self.request.user.id).filter(status=0)
        # Category : 5  출장 문서
        jarvis_list = core_models.jarvis_list.objects.filter(category=5)
        acceptor_list = core_models.acceptor_list.objects.all()
        return render(
            request,
            "groupware/upper_travel_list.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"전자결재",
                "nav_sub_2":"출장여비",
                "nav_sub_3":"출장여비리스트",
                "travel_list":travel_list,
                "jarvis_list":jarvis_list,
                "acceptor_list":acceptor_list,
            },
        )

class upper_travel_report_View(ListView):
       
    def get(self, request):
        travel_list = models.Travel.objects.filter(user_id = self.request.user.id).filter(Q(status=1)|Q(status=2))
        # Category : 6  출장 보고서문서
        return render(
            request,
            "groupware/upper_travel_report.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"전자결재",
                "nav_sub_2":"출장여비",
                "nav_sub_3":"출장리포트작성",
                "travel_list":travel_list,
            },
        )

# 출장 보고서  디테일 뷰
class upper_travel_report_detail_View(DetailView):
    login_url = "users:login"
    def get_queryset(self):
        return models.Travel.objects.filter(pk=self.kwargs["pk"])

    template_name = "groupware/upper_travel_report_detail.html"
    context_object_name = "travel"

    def get_context_data(self, **kwargs):
        detail_model = models.Travel.objects.get(pk=self.kwargs["pk"])
        report_detail_model = models.Travel_report.objects.get(travel_id=self.kwargs["pk"])
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
        # 차량 운행 기록 받아오기
        car_list = models.Travel_report_traffic.objects.filter(travel_report_id=report_detail_model.pk)
        # 숙박비 기록 받아오기
        sleep_list = models.Travel_report_sleep.objects.filter(travel_report_id=report_detail_model.pk)
        # 하이패스 기록 받아오기
        hipass_list = models.Travel_report_hipass.objects.filter(travel_report_id=report_detail_model.pk)        
        # 기타 사용 기록 받아오기
        other_list = models.Travel_report_other.objects.filter(travel_report_id=report_detail_model.pk)
        # 식대 사용 기록 받아오기
        food_list = models.Travel_report_food.objects.filter(travel_report_id=report_detail_model.pk)

        # 최종 비용 계산
        hipass_total = 0
        for hipass in hipass_list:
            hipass_total = hipass_total + hipass.pay 
        food_total = 0
        for food in food_list:
            if food.pay > 8000:
                food_total = food_total + 8000
            else:
                food_total = food_total + food.pay
        other_total = 0
        for other in other_list:
            other_total = other_total + other.pay
        sleep_total = 0
        for sleep in sleep_list:
            if sleep.pay > 60000:
                sleep_total = sleep_total + 60000
            else:
                sleep_total = sleep_total

        total_pay_money = total_money + hipass_total + food_total + other_total + sleep_total

        context = super(upper_travel_report_detail_View, self).get_context_data(**kwargs)
        context["span_day"] = span_day
        context["oil_money"] = oil_money
        context["oil_km_money"] = math.trunc(oil_km_money)
        context["total_money"] = math.trunc(round(total_money,-2)) # 차 기름값

        context["car_list"] = car_list
        context["sleep_list"] = sleep_list
        context["hipass_list"] = hipass_list
        context["other_list"] = other_list
        context["food_list"] = food_list
        context["hipass_total"] = math.trunc(round(hipass_total,-2))
        context["food_total"] = math.trunc(round(food_total,-2))
        context["other_total"] = math.trunc(round(other_total,-2))
        context["sleep_total"] = math.trunc(round(sleep_total,-2))
        context["total_pay_money"] = math.trunc(round(total_pay_money,-2))

        context["nav_main"] = "그룹웨어"
        context["nav_sub_1"] = "전자결재"
        context["nav_sub_2"] = "출장여비"
        context["nav_sub_3"] = "출장여비작성"
        context["span_day"] = span_day
        context["report_detail_model"] = report_detail_model
        
        return context

class upper_travel_report_insert_View(FormView):
    form_class = forms.TravelReportForm
    template_name = "groupware/upper_travel_report_insert.html"
    success_url = reverse_lazy("groupware:upper_travel_report")

    def form_valid(self, form):
        report_data = form.save(commit=False)
        #pk 발행을 위한  DB 임시 저장
        report_data.save()
        travel_list = models.Travel.objects.get(pk=self.kwargs["pk"])
        travle_location = travel_list.location_1
        jarvis_list = core_models.jarvis_list.objects.filter(category=5).get(document_5=travel_list.pk)

        acceptor_list = core_models.acceptor_list.objects.filter(jarvis_no_id=jarvis_list.pk)
        acceptor_1 = acceptor_list[0].acceptor.pk
        acceptor_2 = acceptor_list[1].acceptor.pk
        acceptor_3 = acceptor_list[2].acceptor.pk

        # 운행 거리 입력
        for i in range(1,6):
            if self.request.POST.get("traffic_"+str(i)+"_date"):
                traffic_pay = models.Travel_report_traffic()
                traffic_pay.travel_report = report_data
                if self.request.FILES.get("traffic_"+str(i)+"_img") is not None:
                    traffic_pay.img = self.request.FILES["traffic_"+str(i)+"_img"]
                traffic_pay.date = self.request.POST.get("traffic_"+str(i)+"_date")
                traffic_pay.km = self.request.POST.get("traffic_"+str(i)+"_length")
                traffic_pay.start = self.request.POST.get("traffic_"+str(i)+"_start")
                traffic_pay.end = self.request.POST.get("traffic_"+str(i)+"_end")
                if self.request.POST.get("traffic_"+str(i)+"_oneway") == "on":
                    traffic_pay.oneway = True
                else:
                    traffic_pay.oneway = False
                traffic_pay.save()

        # 하이패스 통행료 입력
        for i in range(1,6):
            if self.request.POST.get("hipass_"+str(i)+"_date"):
                hipass_pay = models.Travel_report_hipass()
                hipass_pay.travel_report = report_data
                if self.request.FILES.get("hipass_"+str(i)+"_img") is not None:
                    hipass_pay.img = self.request.FILES["hipass_"+str(i)+"_img"]
                hipass_pay.date = self.request.POST.get("hipass_"+str(i)+"_date")
                hipass_pay.start = self.request.POST.get("hipass_"+str(i)+"_start")
                hipass_pay.end = self.request.POST.get("hipass_"+str(i)+"_end")
                hipass_pay.pay = self.request.POST.get("hipass_"+str(i)+"_pay")
                hipass_pay.save()
        # 숙소비 입력
        for i in range(1,6):
            if self.request.POST.get("sleep_"+str(i)+"_date"):
                sleep_pay = models.Travel_report_sleep()
                sleep_pay.travel_report = report_data
                if self.request.FILES.get("sleep_"+str(i)+"_img") is not None:
                    sleep_pay.img = self.request.FILES["sleep_"+str(i)+"_img"]
                sleep_pay.date = self.request.POST.get("sleep_"+str(i)+"_date")
                sleep_pay.pay = self.request.POST.get("sleep_"+str(i)+"_pay")
                sleep_pay.save()
        # 기타 여비 입력
        for i in range(1,6):
            if self.request.POST.get("other_"+str(i)+"_date"):
                other_pay = models.Travel_report_other()
                other_pay.travel_report = report_data
                if self.request.FILES.get("other_"+str(i)+"_img") is not None:
                    other_pay.img = self.request.FILES["other_"+str(i)+"_img"]
                other_pay.date = self.request.POST.get("other_"+str(i)+"_date")
                other_pay.comment = self.request.POST.get("other_"+str(i)+"_comment")
                other_pay.pay = self.request.POST.get("other_"+str(i)+"_pay")
                other_pay.save()
        # 식대 여비 입력
        for i in range(1,6):
            if self.request.POST.get("food_"+str(i)+"_date"):
                food_pay = models.Travel_report_food()
                food_pay.travel_report = report_data
                if self.request.FILES.get("food_"+str(i)+"_img") is not None:
                    food_pay.img = self.request.FILES["food_"+str(i)+"_img"]
                food_pay.date = self.request.POST.get("food_"+str(i)+"_date")
                food_pay.pay = self.request.POST.get("food_"+str(i)+"_pay")
                food_pay.save()
        
        # 자비스에 등록
        jarvis_data = core_models.jarvis_list()
        # 6 : 출장 리포트 다큐먼트 코드 번호
        jarvis_data.category = 6
        # 출장 리포트 문서 번호
        jarvis_data.document_6 = report_data.pk
        # 출장 신청서 문서 번호도 기입해준다
        jarvis_data.document_5 = travel_list.pk
        jarvis_data.document_title = "출장 결과 리포트 - "+ str(travle_location)
        jarvis_data.document_user = self.request.user.username
        # 0 : 상신 상태
        jarvis_data.status = 0
        jarvis_data.save()


        # 결제자 등록하기
        acceptor_data = core_models.acceptor_list()
        acceptor_data.jarvis_no = jarvis_data
        tmp = users_models.User.objects.get(pk=acceptor_1)
        acceptor_data.acceptor = tmp
        # 1: 최상위 결제자 
        acceptor_data.priolity = 1
        acceptor_data.result = 3
        acceptor_data.save()
        acceptor_data = core_models.acceptor_list()
        acceptor_data.jarvis_no = jarvis_data
        tmp = users_models.User.objects.get(pk=acceptor_2)
        acceptor_data.acceptor = tmp
        # 2: 김수영대리 
        acceptor_data.priolity = 2
        acceptor_data.result = 3
        acceptor_data.save()
        acceptor_data = core_models.acceptor_list()
        acceptor_data.jarvis_no = jarvis_data
        tmp = users_models.User.objects.get(pk=acceptor_3)
        acceptor_data.acceptor = tmp
        # 3: 팀장
        acceptor_data.priolity = 3
        acceptor_data.result = 3
        acceptor_data.save()

        return redirect(reverse("groupware:upper_travel_report"))

    def get_context_data(self, **kwargs):
        user_list = users_models.User.objects.all()
        travel_list = models.Travel.objects.filter(pk=self.kwargs["pk"])
        detail_model = models.Travel.objects.get(pk=self.kwargs["pk"])
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
        context = super(upper_travel_report_insert_View, self).get_context_data(**kwargs)
        context["span_day"] = span_day
        context["oil_money"] = oil_money
        context["oil_km_money"] = math.trunc(oil_km_money)
        context["total_money"] = math.trunc(round(total_money,-2))
        context["nav_main"] = "그룹웨어"
        context["nav_sub_1"] = "전자결재"
        context["nav_sub_2"] = "출장여비"
        context["nav_sub_3"] = "출장보고서작성"
        context["user_list"] = user_list
        context["travel_list"] = travel_list

        return context

class upper_travel_insult_View(FormView):
    form_class = forms.TravelInsertForm
    template_name = "groupware/upper_travel_insult.html"
    success_url = reverse_lazy("groupware:upper_travel_list")

    def form_valid(self, form):
        travel_data = form.save(commit=False)
        total_km = 0
        if travel_data.reback_1 == 1 and travel_data.location_1 is not None:
            total_km = total_km + (travel_data.km_1*2)
        elif travel_data.location_1 is not None:
            total_km = total_km + travel_data.km_1
        if travel_data.reback_2 == 1 and travel_data.location_1 is not None:
            total_km = total_km + (travel_data.km_2*2)
        elif travel_data.location_2 is not None:
            total_km = total_km + travel_data.km_2
        if travel_data.reback_3 == 1 and travel_data.location_1 is not None:
            total_km = total_km + (travel_data.km_3*2)
        elif travel_data.location_3 is not None:
            total_km = total_km + travel_data.km_3         
        if travel_data.reback_4 == 1 and travel_data.location_1 is not None:
            total_km = total_km + (travel_data.km_4*2)
        elif travel_data.location_4 is not None:
            total_km = total_km + travel_data.km_4
        if travel_data.reback_5 == 1 and travel_data.location_1 is not None:
            total_km = total_km + (travel_data.km_5*2)
        elif travel_data.location_5 is not None:
            total_km = total_km + travel_data.km_5
        travel_data.total_km = total_km
        travel_data.save()

        # 자비스에 등록
        jarvis_data = core_models.jarvis_list()
        # 5 : 출장 다큐먼트 코드 번호
        jarvis_data.category = 5
        # travel 문서 번호
        jarvis_data.document_5 = travel_data.pk
        jarvis_data.document_title = "출장 신청 - "+ str(self.request.POST.get("location_1"))
        jarvis_data.document_user = self.request.user.username
        # 0 : 상신 상태
        jarvis_data.status = 0
        jarvis_data.save()

        # 결제자 폼 받아오기
        if self.request.POST.get("acceptor_1") is not None:
            # 결제자 등록하기
            acceptor_data = core_models.acceptor_list()
            acceptor_data.jarvis_no = jarvis_data
            tmp = users_models.User.objects.get(pk = self.request.POST.get("acceptor_1"))
            acceptor_data.acceptor = tmp
            # 1: 최상위 결제자 
            acceptor_data.priolity = 1
            acceptor_data.result = 3
            acceptor_data.save()

        if self.request.POST.get("acceptor_2") is not None:
            # 결제자 등록하기
            acceptor_data = core_models.acceptor_list()
            acceptor_data.jarvis_no = jarvis_data
            tmp = users_models.User.objects.get(pk = self.request.POST.get("acceptor_2"))
            acceptor_data.acceptor = tmp
            # 2: 두번째 결제자
            acceptor_data.priolity = 2
            acceptor_data.result = 3
            acceptor_data.save()

        if self.request.POST.get("acceptor_3") is not None:
            # 결제자 등록하기
            acceptor_data = core_models.acceptor_list()
            acceptor_data.jarvis_no = jarvis_data
            tmp = users_models.User.objects.get(pk = self.request.POST.get("acceptor_3"))
            acceptor_data.acceptor = tmp
            # 3: 세번째 결제자
            acceptor_data.priolity = 3
            acceptor_data.result = 3
            acceptor_data.save()
        return redirect(reverse("groupware:upper_travel_list"))

    def get_context_data(self, **kwargs):
        user_list = users_models.User.objects.all()
        context = super(upper_travel_insult_View, self).get_context_data(**kwargs)
        context["nav_main"] = "그룹웨어"
        context["nav_sub_1"] = "전자결재"
        context["nav_sub_2"] = "출장여비"
        context["nav_sub_3"] = "출장여비작성"
        context["user_list"] = user_list
        return context

# 작성 출장 신청서 디테일 뷰
class upper_travel_detail_View(DetailView):
    login_url = "users:login"
    def get_queryset(self):
        return models.Travel.objects.filter(pk=self.kwargs["pk"])

    template_name = "groupware/upper_travel_detail.html"
    context_object_name = "travel"

    def get_context_data(self, **kwargs):
        detail_model = models.Travel.objects.get(pk=self.kwargs["pk"])
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
        context["nav_main"] = "그룹웨어"
        context["nav_sub_1"] = "전자결재"
        context["nav_sub_2"] = "출장여비"
        context["nav_sub_3"] = "출장여비작성"
        return context




class upper_buy_list_View(ListView):
       
    def get(self, request):
        return render(
            request,
            "groupware/upper_buy_list.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"전자결재",
                "nav_sub_2":"품의서",
                "nav_sub_3":"품의서리스트",
            },
        )

class upper_buy_insult_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/upper_buy_insult.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"전자결재",
                "nav_sub_2":"품의서",
                "nav_sub_3":"품의서작성",
            },
        )

class upper_pay_list_View(ListView):
       
    def get(self, request):
        return render(
            request,
            "groupware/upper_pay_list.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"전자결재",
                "nav_sub_2":"지출결의서",
                "nav_sub_3":"지출결의서리스트",
            },
        )

class upper_pay_insult_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/upper_pay_insult.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"전자결재",
                "nav_sub_2":"지출결의서",
                "nav_sub_3":"지출결의서작성",
            },
        )

class upper_free_list_View(ListView):
       
    def get(self, request):
        return render(
            request,
            "groupware/upper_free_list.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"전자결재",
                "nav_sub_2":"자유양식",
                "nav_sub_3":"자유양식리스트",
            },
        )

class upper_free_insult_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/upper_free_insult.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"전자결재",
                "nav_sub_2":"자유양식",
                "nav_sub_3":"자유양식작성",
            },
        )

class customer_care_list_View(ListView):
       
    def get(self, request):
        return render(
            request,
            "groupware/customer_care_list.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"고객관리",
                "nav_sub_3":"고객관리리스트",
            },
        )

class customer_care_insult_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/customer_care_insult.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"고객관리",
                "nav_sub_3":"고객관리작성",
            },
        )

class letter_box_list_View(ListView):
       
    def get(self, request):
        return render(
            request,
            "groupware/letter_box_list.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"대외문서관리",
                "nav_sub_3":"대외문서관리리스트",
            },
        )

class letter_box_insult_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/letter_box_insult.html",
            {
                "nav_main":"그룹웨어",
                "nav_sub_1":"대외문서관리",
                "nav_sub_3":"대외문서관리작성",
            },
        )





# 즐겨찾기 팝업
class upper_travel_favo_popup_1_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/popup/upper_travel_favo_popup_1.html",
            {

            },
        )
class upper_travel_favo_popup_2_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/popup/upper_travel_favo_popup_2.html",
            {

            },
        )
class upper_travel_favo_popup_3_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/popup/upper_travel_favo_popup_3.html",
            {

            },
        )
class upper_travel_favo_popup_4_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/popup/upper_travel_favo_popup_4.html",
            {

            },
        )
class upper_travel_favo_popup_5_View(ListView):

    def get(self, request):
        return render(
            request,
            "groupware/popup/upper_travel_favo_popup_5.html",
            {

            },
        )