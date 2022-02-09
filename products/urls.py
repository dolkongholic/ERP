from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("products_list/", views.products_list_View.as_view(), name="products_list"),   #재고>품목관리>품목 리스트
    path("products_insult/", views.products_insult_View.as_view(), name="products_insult"), #재고>품목관리>품목추가
    path("companies_list/", views.companies_list_View.as_view(), name="companies_list"),    #재고>기초등록>거래처 리스트
    path("companies_insult/", views.companies_insult_View.as_view(), name="companies_insult"),  # 재고>기초등록>거래처 등록
    path("companies_group_list/", views.companies_group_list_View.as_view(), name="companies_group_list"),  # 재고>기초등록>거래처 그룹 리스트
    path("companies_group_insert/", views.companies_group_insert_View.as_view(), name="companies_group_insert"),  # 재고>기초등록>거래처 그룹 추가
    path("products_now_list/", views.products_now_list_View.as_view(), name="products_now_list"),   #재고>자재관리>재고현황
    path("products_now_history/", views.products_now_history_View.as_view(), name="products_now_history"),  # 재고>자재관리>반입반출 내역서
    path("products_buy_list/", views.products_buy_list_View.as_view(), name="products_buy_list"),   # 재고>자재관리>발주서>발주서 현황
    path("products_buy_insult/", views.products_buy_insult_View.as_view(), name="products_buy_insult"), # 재고>자재관리>발주서>발주서 추가
    path("products_plan_list/", views.products_plan_list_View.as_view(), name="products_plan_list"),    # 재고>자재관리>견적서>견적서 현황
    path("products_plan_insult/", views.products_plan_insult_View.as_view(), name="products_plan_insult"),  # 재고>자재관리>견적서>견적서 추가
    
]
