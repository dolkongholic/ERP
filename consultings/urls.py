from django.urls import path
from . import views

app_name = "consultings"

urlpatterns = [
    path("consultings_plan_list/", views.consultings_plan_list_View.as_view(), name="consultings_plan_list"), 
    path("consultings_plan_insult/", views.consultings_plan_insult_View.as_view(), name="consultings_plan_insult"), 
]
