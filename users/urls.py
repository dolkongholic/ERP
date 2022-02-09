from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.Login_View.as_view(), name="login"), #로그인 페이지
    path("mypage/", views.MyPage_View.as_view(), name="mypage"), #메인 - 마이페이지
    path("Group/", views.Group_View.as_view(), name="group"), # 조직도
    path("InsultUser/", views.InsultUser_View.as_view(), name="insult_user"), # 사원등록
    path("Print/", views.Print_View.as_view(), name="print"), #증명서 인쇄
    path("file_box/", views.FileBox_View.as_view(), name="file_box"), #계약서 관리
    ############################################# 근태 - 항목 관리 ##############################################
    path("vacation_list/", views.vacation_list_View.as_view(), name="vacation_list"), # 근태 - 항목리스트
    path("vacation_list/delete/<int:pk>", views.delete_vacation_list, name="vacation_list_del"), # 근태 - 항목리스트 삭제
    path("vacation_list/update/<int:pk>", views.vacation_list_update_View.as_view(), name="vacation_list_update"), # 근태 - 항목리스트 수정
    path("vacation_list_insult/", views.vacation_list_insult_View.as_view(), name="vacation_list_insult"), # 근태 - 항목추가
    ############################################# 근태 - 휴가 사용 ##############################################
    path("vacation_use_list/", views.vacation_use_list_View.as_view(), name="vacation_use_list"), # 근태 - 휴가사용실적현황 리스트
    path("vacation_use/delete/<int:pk>", views.delete_vacation_list, name="vacation_use_del"), # 근태 - 휴가사용실적현황 리스트 삭제
    path("vacation_use/update/<int:pk>", views.vacation_use_update_View.as_view(), name="vacation_use_update"), # 근태 - 휴가사용실적현황 리스트 수정
    path("vacation_use_insult/", views.vacation_use_insult_View.as_view(), name="vacation_use_insult"), # 근태 - 휴가사용실적현황 추가
    path("vacation_use/result/yes/<int:pk>", views.vacation_use_result_yes, name="vacation_use_result_yes"), # 근태 - 휴가사용실적현황 결재 승인
    path("vacation_use/result/no/<int:pk>", views.vacation_use_result_no, name="vacation_use_result_no"), # 근태 - 휴가사용실적현황 결재 반려
    path("vacation_use/result/re/<int:pk>", views.vacation_use_result_re, name="vacation_use_result_re"), # 근태 - 휴가사용실적현황 결재 재상신
    path("vacation_use/result/del/<int:pk>", views.vacation_use_result_del, name="vacation_use_result_del"), # 근태 - 휴가사용실적현황 결재 삭제
    ############################################# 근태 - 휴가 사용 ##############################################
    path("vacation_remain/", views.vacation_remain_View.as_view(), name="vacation_remain"), # 근태 - 휴가사용실적현황 리스트
    #############################################  결재 대기 ##############################################
    path("ready/", views.ready_View.as_view(), name="ready"), # 결재 대기 리스트
    
    
]
