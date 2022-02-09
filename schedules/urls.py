from django.urls import path
from . import views

app_name = "schedules"

urlpatterns = [
    path("group_schedule/", views.GroupSchedul_View.as_view(), name="group_schedule"),
    path("plan_schedule/", views.PlanSchedul_View.as_view(), name="plan_schedule"),
    path("cancel_schedule/", views.CancelSchedul_View.as_view(), name="cancel_schedule"),
]
