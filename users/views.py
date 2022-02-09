import datetime
from telnetlib import STATUS
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import View,FormView,UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q

from core import models as core_models
from . import forms, models

class Login_View(FormView):

    form_class = forms.LoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = models.User.objects.get(email=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:index")

# class Index_View(mixins.LoggedInOnlyView, View):
class MyPage_View(View):
    def get(self, request):
        return render(
            request,
            "users/mypage.html",
            {
                # "context": person_1_conunt,
            },
        )

class InsultUser_View(FormView):
    template_name = "users/insult_user.html"
    form_class = forms.SignUpForm

    def form_valid(self, form):
        Project = form.save()
        Project.save()
        return redirect(reverse("users:mypage"))

    def get_context_data(self, **kwargs):
        context = super(InsultUser_View, self).get_context_data(**kwargs)
        context["nav_main"] = "인사/근태"
        context["nav_sub_1"] = "인사"
        context["nav_sub_2"] = "사원등록"
        return context

class Group_View(View):
    def get(self, request): 
        users = models.User.objects.all()
        return render(
            request,
            "users/group.html",
            {
                "nav_main":"인사/근태",
                "nav_sub_1":"인사",
                "nav_sub_2":"조직도",
                "users" : users,

            },
        )

class Print_View(View):
    def get(self, request):
        return render(
            request,
            "users/print.html",
            {
                "nav_main":"인사/근태",
                "nav_sub_1":"인사",
                "nav_sub_2":"증명서인쇄",

            },
        )

class FileBox_View(View):
    def get(self, request):
        return render(
            request,
            "users/file_box.html",
            {
                "nav_main":"인사/근태",
                "nav_sub_1":"인사",
                "nav_sub_2":"계약서관리",

            },
        )


######################################################################## 근태 - 항목 관리

# 근태 항목 추가
class vacation_list_insult_View(FormView):
    template_name = "users/vacation_list_insult.html"
    form_class = forms.VacationListForm

    def form_valid(self, form):
        Project = form.save()
        Project.save()
        return redirect(reverse("users:vacation_list"))

    def get_context_data(self, **kwargs):
        users = models.User.objects.all()
        context = super(vacation_list_insult_View, self).get_context_data(**kwargs)
        context["nav_main"] = "인사/근태"
        context["nav_sub_1"] = "근태"
        context["nav_sub_2"] = "항목관리"
        context["nav_sub_3"] = "항목추가"
        context["users"] = users
        return context

# 근태 항목관리 리스트
class vacation_list_View(View):
    def get(self, request):
        vacation_list = models.VacationList.objects.all()
        return render(
            request,
            "users/vacation_list.html",
            {
                "nav_main":"인사/근태",
                "nav_sub_1":"근태",
                "nav_sub_2":"항목관리",
                "nav_sub_3":"항목리스트",
                "vacation_list":vacation_list,
            },
        )
# 근태 항목 수정
class vacation_list_update_View(UpdateView):
    def get_queryset(self):
        return models.VacationList.objects.filter(pk=self.kwargs["pk"])

    template_name = "users/vacation_list_update.html"
    
    fields = (
        "type",
        "add_date",
        "start_date",
        "end_date",
        "target_people",
    )

    def get_success_url(self):
        return reverse("users:vacation_list")

    def get_context_data(self, **kwargs):
        users = models.User.objects.all()
        datas = models.VacationList.objects.filter(pk=self.kwargs["pk"])
        context = super(vacation_list_update_View, self).get_context_data(**kwargs)
        context["nav_main"] = "인사/근태"
        context["nav_sub_1"] = "근태"
        context["nav_sub_2"] = "항목관리"
        context["nav_sub_3"] = "항목추가"
        context["users"] = users
        context["datas"] = datas
        return context
        
# 근태 항목 삭제
def delete_vacation_list(request, pk):
    user = request.user
    try:
        models.VacationList.objects.get(pk=pk)
        if user.is_staff:
            models.VacationList.objects.filter(pk=pk).delete()
        else:
            print("권한이 없습니다.")
        return redirect(reverse("users:vacation_list"))
    except models.VacationList.DoesNotExist:
        return redirect(reverse("users:vacation_list"))


######################################################################## 근태 - 휴가 사용 실적 현황

# 근태 - 휴가 추가
class vacation_use_insult_View(FormView):
    template_name = "users/vacation_use_insult.html"
    form_class = forms.VacationUseForm

    def form_valid(self, form):
        Project = form.save()
        Project.save()
        return redirect(reverse("users:vacation_use_list"))

    def get_context_data(self, **kwargs):
        vacation_list = models.VacationList.objects.filter(target_people=self.request.user.pk)

        for vacation in vacation_list:
            try:
                check_model = models.VacationUse.objects.filter(type_id=vacation.pk)
                day_count = vacation.add_date
                for check in check_model:
                    tmp_date_check = (check.end_date - check.start_date).days + 1
                    if check.end_date == check.start_date:
                        tmp_date_check = 2

                    if not check.start_date_morning :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.start_date_afternoon :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.end_date_morning :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.end_date_afternoon :
                        tmp_date_check = tmp_date_check - 0.5
                    day_count = day_count - tmp_date_check
                    if day_count <= 0:
                        vacation_list = vacation_list.filter(~Q(id=check.type_id))
               
            except models.VacationUse.DoesNotExist:
                continue;
        accepter_1 = models.User.objects.filter(staff_level=0)
        accepter_2 = models.User.objects.filter(staff_level=1)

        context = super(vacation_use_insult_View, self).get_context_data(**kwargs)
        context["nav_main"] = "인사/근태"
        context["nav_sub_1"] = "근태"
        context["nav_sub_2"] = "휴가사용실적현황"
        context["nav_sub_3"] = "휴가사용실적리스트"
        context["vacation_list"] = vacation_list
        context["accepter_1"] = accepter_1
        context["accepter_2"] = accepter_2
        return context


# 근태 휴가 사용 리스트
class vacation_use_list_View(View):
    def get(self, request):
        vacation_list = models.VacationUse.objects.all()
        return render(
            request,
            "users/vacation_use_list.html",
            {
                "nav_main":"인사/근태",
                "nav_sub_1":"근태",
                "nav_sub_2":"휴가사용실적현황",
                "nav_sub_3":"휴가사용실적리스트",
                "vacation_list":vacation_list,
            },
        )
# 근태 항목 수정
class vacation_use_update_View(UpdateView):
    def get_queryset(self):
        return models.VacationUse.objects.filter(pk=self.kwargs["pk"])

    template_name = "users/vacation_use_update.html"
    
    fields = (
        "type",
        "add_date",
        "start_date",
        "end_date",
        "target_people",
    )

    def get_success_url(self):
        return reverse("users:vacation_use_list")

    def get_context_data(self, **kwargs):
        users = models.User.objects.all()
        datas = models.VacationUse.objects.filter(pk=self.kwargs["pk"])
        context = super(vacation_use_update_View, self).get_context_data(**kwargs)
        context["nav_main"] = "인사/근태"
        context["nav_sub_1"] = "근태"
        context["nav_sub_2"] = "휴가사용실적현황"
        context["nav_sub_3"] = "휴가사용"
        context["users"] = users
        context["datas"] = datas
        return context
        
# 근태 항목 삭제
def delete_vacation_use(request, pk):
    user = request.user
    try:
        models.VacationUse.objects.get(pk=pk)
        if user.is_staff:
            models.VacationUse.objects.filter(pk=pk).delete()
        else:
            print("권한이 없습니다.")
        return redirect(reverse("users:vacation_use_list"))
    except models.VacationList.DoesNotExist:
        return redirect(reverse("users:vacation_use_list"))


# 잔여휴가현황 리스트
class vacation_remain_View(View):
    def get(self, request):

        vacation_list = models.VacationList.objects.filter(target_people=self.request.user.pk)
        result_list = {}
        for vacation in vacation_list:
            try:
                check_model = models.VacationUse.objects.filter(type_id=vacation.pk)
                day_count = vacation.add_date
                result_list[vacation.id] = {
                        "type" : vacation.type,
                        "start_date" : vacation.start_date,
                        "end_date" : vacation.end_date,
                        "remain_date" : day_count,
                    }
                for check in check_model:
                    tmp_date_check = (check.end_date - check.start_date).days + 1
                    if check.end_date == check.start_date:
                        tmp_date_check = 2

                    if not check.start_date_morning :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.start_date_afternoon :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.end_date_morning :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.end_date_afternoon :
                        tmp_date_check = tmp_date_check - 0.5
                    day_count = day_count - tmp_date_check
                    if day_count <= 0:
                        del(result_list[vacation.id])
                    else :
                        result_list[vacation.id] = {
                                'type' : check.type,
                                'start_date' : check.start_date,
                                'end_date' : check.end_date,
                                'remain_date' : day_count,
                            }
            except models.VacationUse.DoesNotExist:
                    print("쿼리 못찾음")

        return render(
            request,
            "users/vacation_remain.html",
            {
                "nav_main":"인사/근태",
                "nav_sub_1":"근태",
                "nav_sub_2":"잔여휴가현황",
                "vacation_list":result_list,
            },
        )


############################## 결제 대기 #########################
class ready_View(View):
    def get(self, request):
        acceptor_list = core_models.acceptor_list.objects.filter(acceptor_id=self.request.user.pk).all()
        vacation_ready_list = models.VacationUse.objects.filter((Q(accepter_1_id=request.user.pk)) | (Q(accepter_2_id = request.user.pk)))
        return render(
            request,
            "users/ready.html",
            {
                "nav_main":"마이페이지",
                "nav_sub_1":"결재대기",
                "vacation_ready_list":vacation_ready_list,
                "acceptor_list":acceptor_list,
            },
        )

# 휴가 결재 승인
def vacation_use_result_yes(request, pk):
    user = request.user
    try:
        vacation = models.VacationUse.objects.get(pk=pk)
        if vacation.accepter_1_id == user.id :
            vacation.accepter_1_result = 1
        elif vacation.accepter_2_id == user.id :
            vacation.accepter_2_result = 1
        vacation.save()

        return redirect(reverse("users:ready"))
    except models.VacationList.DoesNotExist:
        return redirect(reverse("users:ready"))

# 휴가 결재 반려
def vacation_use_result_no(request, pk):
    user = request.user
    try:
        vacation = models.VacationUse.objects.get(pk=pk)
        if vacation.accepter_1_id == user.id :
            vacation.accepter_1_result = 2
        elif vacation.accepter_2_id == user.id :
            vacation.accepter_2_result = 2
        vacation.save()

        return redirect(reverse("users:ready"))
    except models.VacationList.DoesNotExist:
        return redirect(reverse("users:ready"))

# 휴가 결재 재상신
def vacation_use_result_re(request, pk):
    user = request.user
    try:
        vacation = models.VacationUse.objects.get(pk=pk)
        vacation.accepter_1_result = 0
        vacation.accepter_2_result = 0
        vacation.save()

        return redirect(reverse("users:vacation_use_list"))
    except models.VacationList.DoesNotExist:
        return redirect(reverse("users:vacation_use_list"))

# 휴가 결재 삭제
def vacation_use_result_del(request, pk):
    user = request.user
    try:
        models.VacationUse.objects.get(pk=pk)
        if user.is_staff:
            models.VacationUse.objects.filter(pk=pk).delete()
        else:
            print("권한이 없습니다.")
        return redirect(reverse("users:vacation_use_list"))
    except models.VacationList.DoesNotExist:
        return redirect(reverse("users:vacation_use_list"))