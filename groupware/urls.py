from django.urls import path
from . import views

app_name = "groupware"

urlpatterns = [
    path("upper_travel_list", views.upper_travel_list_View.as_view(), name="upper_travel_list"), # 전자결재 > 출장여비 리스트
    path("upper_travel_report", views.upper_travel_report_View.as_view(), name="upper_travel_report"), # 전자결재 > 출장 리포트 리스트
    path("upper_travel_report_insert/<int:pk>", views.upper_travel_report_insert_View.as_view(), name="upper_travel_report_insert"), # 전자결재 > 출장 리포트 작성
    
    path("upper_travel_report_detail/<int:pk>", views.upper_travel_report_detail_View.as_view(), name="upper_travel_report_detail"), # 전자결재 > 출장 리포트 작성
    path("upper_travel_insult", views.upper_travel_insult_View.as_view(), name="upper_travel_insult"), # 전자결재 > 출장여비 작성
    path("upper_travel_detail/<int:pk>", views.upper_travel_detail_View.as_view(), name="upper_travel_detail"), # 전자결재 > 출장여비 디테일
    path("upper_buy_list", views.upper_buy_list_View.as_view(), name="upper_buy_list"),  # 전자결재 > 품의서 리스트
    path("upper_buy_insult", views.upper_buy_insult_View.as_view(), name="upper_buy_insult"),  #전자결재 > 품의서 작성
    path("upper_pay_list", views.upper_pay_list_View.as_view(), name="upper_pay_list"),  # 전자결재 > 지출결의서 리스트
    path("upper_pay_insult", views.upper_pay_insult_View.as_view(), name="upper_pay_insult"), # 전자결재 > 지출결의서 작성
    path("upper_free_list", views.upper_free_list_View.as_view(), name="upper_free_list"), # 전자결재 > 자유양식 리스트
    path("upper_free_insult", views.upper_free_insult_View.as_view(), name="upper_free_insult"),  # 전자결재 > 자유양식 작성
    path("customer_care_list", views.customer_care_list_View.as_view(), name="customer_care_list"), # 전자결재 > 고객관리 리스트
    path("customer_care_insult", views.customer_care_insult_View.as_view(), name="customer_care_insult"),  # 전자결재 > 고객관리 작성
    path("letter_box_list", views.letter_box_list_View.as_view(), name="letter_box_list"), # 전자결재 > 대외문서관리 리스트
    path("letter_box_insult", views.letter_box_insult_View.as_view(), name="letter_box_insult"),  # 전자결재 > 대외문서관리 작성
    
path("upper_travel_favo_popup_1/", views.upper_travel_favo_popup_1_View.as_view(), name="upper_travel_favo_popup_1"), # 즐겨찾기 팝업
path("upper_travel_favo_popup_2/", views.upper_travel_favo_popup_2_View.as_view(), name="upper_travel_favo_popup_2"), # 즐겨찾기 팝업
path("upper_travel_favo_popup_3/", views.upper_travel_favo_popup_3_View.as_view(), name="upper_travel_favo_popup_3"), # 즐겨찾기 팝업
path("upper_travel_favo_popup_4/", views.upper_travel_favo_popup_4_View.as_view(), name="upper_travel_favo_popup_4"), # 즐겨찾기 팝업
path("upper_travel_favo_popup_5/", views.upper_travel_favo_popup_5_View.as_view(), name="upper_travel_favo_popup_5"), # 즐겨찾기 팝업
]
