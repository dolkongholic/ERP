import datetime
from django import forms
from django.db.models import Q
from . import models
from django.contrib import messages


class VacationUseForm(forms.ModelForm):
    class Meta:
        model = models.VacationUse
        fields = (
            "type",
            "start_date",
            "end_date",
            "user",
            "comment",
            "start_date_morning",
            "start_date_afternoon",
            "end_date_morning",
            "end_date_afternoon",
            "accepter_1",
            "accepter_2",
        )
    def clean(self):
        type = self.cleaned_data.get("type")
        days = 0
        if self.cleaned_data.get("start_date_morning") :
            days = days - 0.5
        if self.cleaned_data.get("start_date_afternoon") :
            days = days - 0.5
        if self.cleaned_data.get("end_date_morning") :
            days = days - 0.5
        if self.cleaned_data.get("end_date_afternoon") :
            days = days - 0.5
        start_date = self.cleaned_data.get("start_date")
        if start_date is not None:
            start_date_re = datetime.datetime.strftime(start_date,'%Y-%m-%d')

        end_date = self.cleaned_data.get("end_date")
        if end_date is not None:
            end_date_re = datetime.datetime.strftime(end_date,'%Y-%m-%d')
        if (start_date and end_date is not None) and (start_date_re > end_date_re):
            self.add_error("end_date", forms.ValidationError("시작일이 종료일 보다 늦을순 없습니다."))

        vacation_list = models.VacationList.objects.filter(type=self.cleaned_data.get("type"))
        for vacation in vacation_list:
            try:
                check_model = models.VacationUse.objects.filter(type_id=vacation.pk)
                day_count = vacation.add_date
                for check in check_model:
                    tmp_date_check = (check.end_date - check.start_date).days + 1
                    
                    if check.end_date == check.start_date:
                        tmp_date_check = 2

                    if not check.start_date_morning :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.start_date_afternoon :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.end_date_morning :
                        tmp_date_check = tmp_date_check - 0.5
                    if not check.end_date_afternoon :
                        tmp_date_check = tmp_date_check - 0.5
                    day_count = day_count - tmp_date_check
            except models.VacationUse.DoesNotExist:
                continue;
        if end_date is not None and start_date is not None:
            if (day_count - abs(((end_date-start_date).days + days))) < 0:
                self.add_error("end_date", forms.ValidationError("잔여일 보다 많이 사용 할수 없습니다. *  %s 잔여일 : %0.1f 일 * " %(type,day_count)))

class VacationListForm(forms.ModelForm):
    class Meta:
        model = models.VacationList
        fields = (
            "type",
            "add_date",
            "start_date",
            "end_date",
            "target_people",
        )
    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        if start_date is not None:
            start_date_re = datetime.datetime.strftime(start_date,'%Y-%m-%d')

        end_date = self.cleaned_data.get("end_date")
        if end_date is not None:
            end_date_re = datetime.datetime.strftime(end_date,'%Y-%m-%d')
        if (start_date and end_date is not None) and (start_date_re > end_date_re):
            self.add_error("end_date", forms.ValidationError("시작일이 종료일 보다 늦을순 없습니다."))

        target_people = self.cleaned_data.get("target_people")
        if target_people is None:
            self.add_error("target_people", forms.ValidationError("대상자를 선택하셔야합니다."))

        
        
        
            

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "user_number",
            "username",
            "password",
            "name_en",
            "people_number",
            "team_code",
            "level",
            "phone",
            "email",
            "address",
            "comment",
            "avatar",
            "account_pic",
            "people_card",
            "poeple_papper",
            "date_in",
            "date_type",
            "date_out",
            "out_comment",
            "bank",
            "account",
            "account_ower",
            "graduation",
            "cert",
            "language",
        )


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "email",
            "password",
        )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.password == password:
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("패스워드가 정확하지 않습니다."))
                print("Password is wrong")
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("사용자가 존재하지 않습니다."))
            print("User does not exist")
            

