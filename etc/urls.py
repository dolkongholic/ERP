from django.urls import path
from . import views

app_name = "etc"

urlpatterns = [
    path("etc_books_list/", views.etc_books_list_View.as_view(), name="etc_books_list"), 
    path("etc_books_insult/", views.etc_books_insult_View.as_view(), name="etc_books_insult"), 
    path("etc_parking_list/", views.etc_parking_list_View.as_view(), name="etc_parking_list"), 
    path("etc_parking_insult/", views.etc_parking_insult_View.as_view(), name="etc_parking_insult"), 
]
