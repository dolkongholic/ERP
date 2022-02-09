from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("estimate/", views.Estimate_View.as_view(), name="estimate"),
    path("estimate_result/", views.EstimateResult_View.as_view(), name="estimate_result"),
]
