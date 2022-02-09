from django.shortcuts import render
from django.views.generic import View,ListView

# class Index_View(mixins.LoggedInOnlyView, View):
class etc_books_list_View(ListView):

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
            "etc/etc_books_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기타",
                "nav_sub_2":"기타교재재고관리",
                "nav_sub_3":"교재재고현황",
            },
        )
class etc_books_insult_View(ListView):

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
            "etc/etc_books_insult.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기타",
                "nav_sub_2":"기타교재재고관리",
                "nav_sub_3":"교재구매판매",
            },
        )

class etc_parking_list_View(ListView):

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
            "etc/etc_parking_list.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기타",
                "nav_sub_2":"기타주차권관리",
                "nav_sub_3":"주차권구매",
            },
        )
class etc_parking_insult_View(ListView):

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
            "etc/etc_parking_insult.html",
            {
                "nav_main":"재고",
                "nav_sub_1":"기타",
                "nav_sub_2":"기타주차권관리",
                "nav_sub_3":"주차권구매판매",
            },
        )
