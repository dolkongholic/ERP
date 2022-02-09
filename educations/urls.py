from django.urls import path
from . import views

app_name = "educations"

urlpatterns = [
    path("educations_buy_list/", views.educations_buy_list_View.as_view(), name="educations_buy_list"),
    path("educations_plan_list/", views.educations_plan_list_View.as_view(), name="educations_plan_list"), 
    path("educations_buy_insult/", views.educations_buy_insult_View.as_view(), name="educations_buy_insult"),
    path("educations_plan_insult/", views.educations_plan_insult_View.as_view(), name="educations_plan_insult"), 
]
