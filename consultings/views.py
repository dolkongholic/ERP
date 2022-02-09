from django.shortcuts import render
from django.views.generic import View,ListView

# class Index_View(mixins.LoggedInOnlyView, View):
class consultings_plan_list_View(ListView):

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
            "consultings/consultings_plan_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기술",
                "nav_sub_2":"기술견적서",
                "nav_sub_3":"견적서현황",
            },
        )

class consultings_plan_insult_View(ListView):

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
            "consultings/consultings_plan_insult.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기술",
                "nav_sub_2":"기술견적서",
                "nav_sub_3":"견적서작성",
            },
        )