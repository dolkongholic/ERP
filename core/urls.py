from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.Index_View.as_view(), name="index"),
    path("upper_success/<int:pk>/<int:category>", views.upper_success_View.as_view(), name="upper_success"),
    path("upper_fail/<int:pk>/<int:category>", views.upper_fail_View.as_view(), name="upper_fail"),
    path("upper_travel_detail/<int:pk>", views.upper_travel_detail_View.as_view(), name="upper_travel_detail"), # 전자결재 > 출장여비 디테일
    path("upper_travel_report_detail/<int:pk>", views.upper_travel_report_detail_View.as_view(), name="upper_travel_report_detail"), # 전자결재 > 출장여비 디테일
]
