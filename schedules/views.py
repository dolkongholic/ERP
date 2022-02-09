from django.shortcuts import render
from django.views.generic import View
from core import models
from users import models as user_model
from groupware import models as groupware_models

# class Index_View(mixins.LoggedInOnlyView, View):
class GroupSchedul_View(View):
    def get(self, request):
        vacation_list = user_model.VacationUse.objects.all()
        vacation_result = {}
        for vacation in vacation_list:
            vacation_result[vacation.id] = {
                'title':vacation.type,
                'user':vacation.user.username,
                'start':str(vacation.start_date.strftime('%Y-%m-%d')),
                'end':str(vacation.end_date.strftime('%Y-%m-%d')),
            }
        travel_list = groupware_models.Travel.objects.all()
        travel_result = {}
        for travel in travel_list:
            travel_result[travel.id] = {
                'title':travel.location_1,
                'user':travel.user.username,
                'start':str(travel.start_date.strftime('%Y-%m-%d')),
                'end':str(travel.end_date.strftime('%Y-%m-%d')),
            }
        return render(
            request,
            "schedules/group_schedule.html",
            {
                "vacation_list": vacation_result,
                "travel_list":travel_result,
            },
        )

class PlanSchedul_View(View):
    def get(self, request):
        return render(
            request,
            "schedules/group_schedule_plan.html",
            {
                # "context": person_1_conunt,
            },
        )

class CancelSchedul_View(View):
    def get(self, request):
        return render(
            request,
            "schedules/group_schedule_cancel.html",
            {
                # "context": person_1_conunt,
            },
        )
