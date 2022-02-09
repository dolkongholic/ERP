import datetime
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import View,FormView,UpdateView,ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from . import forms, models

######################################################################## 기재고 - 기초등록 - 품목 관리
# 품목리스트
class products_list_View(ListView):
        
    def get(self, request):
        products_list = models.Product.objects.all()
        return render(
            request,
            "products/products_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기초등록",
                "nav_sub_2":"품목관리",
                "nav_sub_3":"품목현황",
                "products_list":products_list,
            },
        )

#  품목추가
class products_insult_View(FormView):
    template_name = "products/products_insult.html"
    form_class = forms.productForm

    def form_valid(self, form):
        Project = form.save()
        Project.save()
        return redirect(reverse("products:products_list"))

    def get_context_data(self, **kwargs):
        context = super(products_insult_View, self).get_context_data(**kwargs)
        context["nav_main"] = "재고"
        context["nav_sub_1"] = "기초등록"
        context["nav_sub_2"] = "품목관리"
        context["nav_sub_3"] = "품목작성"
        return context


class companies_list_View(ListView):

    # login_url = "users:login"

    # def get_queryset(self):
    #     return models.Inspection.objects.filter(auth=self.request.user.id)

    # template_name = "inspections/inspection_list.html"

    # context_object_name = "inspections"

    # def get_context_data(self, **kwargs):

    #     context = super(list_View, self).get_context_data(**kwargs)
    #     return context
        
    def get(self, request):
        return render(
            request,
            "products/companies_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기초등록",
                "nav_sub_2":"거래처관리",
                "nav_sub_3":"거래처현황",
            },
        )
class companies_insult_View(FormView):

    # login_url = "users:login"

    form_class = forms.companiesForm
    template_name = "products/companies_insert.html"
    success_url = reverse_lazy("products:companies_list")

    def form_valid(self, form):
        data = form.save(commit=False)
        #pk 발행을 위한  DB 임시 저장
        data.save()
        return redirect(reverse("products:companies_list"))

    def get_context_data(self, **kwargs):
        context = super(companies_insult_View, self).get_context_data(**kwargs)
        context["nav_main"] = "재고",
        context["nav_sub_1"] = "기초등록",
        context["nav_sub_2"] = "거래처관리",
        context["nav_sub_3"] = "거래처작성",

        return context

class companies_group_list_View(ListView):
        
    def get(self, request):
        company_group_list = models.Company_group.objects.all()
        return render(
            request,
            "products/companies_group_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기초등록",
                "nav_sub_2":"거래처그룹관리",
                "nav_sub_3":"거래처그룹리스트",
                "company_list":company_group_list,
            },
        )

class companies_group_insert_View(FormView):
    # login_url = "users:login"

    form_class = forms.companiesGroupForm
    template_name = "products/companies_group_insert.html"
    success_url = reverse_lazy("products:companies_group_list")

    def form_valid(self, form):
        data = form.save(commit=False)
        #pk 발행을 위한  DB 임시 저장
        data.save()
        return redirect(reverse("products:companies_group_list"))

    def get_context_data(self, **kwargs):
        context = super(companies_group_insert_View, self).get_context_data(**kwargs)
        context["nav_main"] = "재고",
        context["nav_sub_1"] = "기초등록",
        context["nav_sub_2"] = "거래처그룹관리",
        context["nav_sub_3"] = "거래처그룹작성",


class products_now_list_View(ListView):

    # login_url = "users:login"

    # def get_queryset(self):
    #     return models.Inspection.objects.filter(auth=self.request.user.id)

    # template_name = "inspections/inspection_list.html"

    # context_object_name = "inspections"

    # def get_context_data(self, **kwargs):

    #     context = super(list_View, self).get_context_data(**kwargs)
    #     return context
        
    def get(self, request):
        return render(
            request,
            "products/products_now_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"자재관리",
                "nav_sub_2":"자재관리재고현황",
                "nav_sub_3":"재고현황",
            },
        )

class products_now_history_View(ListView):

    # login_url = "users:login"

    # def get_queryset(self):
    #     return models.Inspection.objects.filter(auth=self.request.user.id)

    # template_name = "inspections/inspection_list.html"

    # context_object_name = "inspections"

    # def get_context_data(self, **kwargs):

    #     context = super(list_View, self).get_context_data(**kwargs)
    #     return context
        
    def get(self, request):
        return render(
            request,
            "products/products_now_history.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"자재관리",
                "nav_sub_2":"자재관리재고현황",
                "nav_sub_3":"반입반출내역서",
            },
        )

class products_buy_list_View(ListView):

    # login_url = "users:login"

    # def get_queryset(self):
    #     return models.Inspection.objects.filter(auth=self.request.user.id)

    # template_name = "inspections/inspection_list.html"

    # context_object_name = "inspections"

    # def get_context_data(self, **kwargs):

    #     context = super(list_View, self).get_context_data(**kwargs)
    #     return context
        
    def get(self, request):
        return render(
            request,
            "products/products_buy_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"자재관리",
                "nav_sub_2":"자재관리발주서",
                "nav_sub_3":"발주서현황",
            },
        )

class products_buy_insult_View(ListView):

    # login_url = "users:login"

    # def get_queryset(self):
    #     return models.Inspection.objects.filter(auth=self.request.user.id)

    # template_name = "inspections/inspection_list.html"

    # context_object_name = "inspections"

    # def get_context_data(self, **kwargs):

    #     context = super(list_View, self).get_context_data(**kwargs)
    #     return context
        
    def get(self, request):
        return render(
            request,
            "products/products_buy_insult.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"자재관리",
                "nav_sub_2":"자재관리발주서",
                "nav_sub_3":"발주서작성",
            },
        )

class products_plan_list_View(ListView):

    # login_url = "users:login"

    # def get_queryset(self):
    #     return models.Inspection.objects.filter(auth=self.request.user.id)

    # template_name = "inspections/inspection_list.html"

    # context_object_name = "inspections"

    # def get_context_data(self, **kwargs):

    #     context = super(list_View, self).get_context_data(**kwargs)
    #     return context
        
    def get(self, request):
        return render(
            request,
            "products/products_plan_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"자재관리",
                "nav_sub_2":"자재관리견적서",
                "nav_sub_3":"견적서현황",
            },
        )

class products_plan_insult_View(ListView):

    # login_url = "users:login"

    # def get_queryset(self):
    #     return models.Inspection.objects.filter(auth=self.request.user.id)

    # template_name = "inspections/inspection_list.html"

    # context_object_name = "inspections"

    # def get_context_data(self, **kwargs):

    #     context = super(list_View, self).get_context_data(**kwargs)
    #     return context
        
    def get(self, request):
        return render(
            request,
            "products/products_plan_insult.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"자재관리",
                "nav_sub_2":"자재관리견적서",
                "nav_sub_3":"견적서작성",
            },
        )