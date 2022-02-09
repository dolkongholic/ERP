from django.shortcuts import render
from django.views.generic import View,ListView

# class Index_View(mixins.LoggedInOnlyView, View):
class educations_buy_list_View(ListView):

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
            "educations/educations_buy_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"교육",
                "nav_sub_2":"교육발주서",
                "nav_sub_3":"발주서현황",
            },
        )

class educations_buy_insult_View(ListView):

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
            "educations/educations_buy_insult.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"교육",
                "nav_sub_2":"교육발주서",
                "nav_sub_3":"발주서작성",
            },
        )

class educations_plan_list_View(ListView):

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
            "educations/educations_plan_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"교육",
                "nav_sub_2":"교육견적서",
                "nav_sub_3":"견적서현황",
            },
        )

class educations_plan_insult_View(ListView):

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
            "educations/educations_plan_insult.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"교육",
                "nav_sub_2":"교육견적서",
                "nav_sub_3":"견적서작성",
            },
        )