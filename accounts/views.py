from django.shortcuts import render
from django.views.generic import View
import random
import numpy as np

class Estimate_View(View):

    def get(self, request):
        return render(
            request,
            "accounts/estimate.html",
            {
                'nav_main':"회계",
                'nav_sub_1':"적격심사견적",
            },
        )

class EstimateResult_View(View):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            base_money = int(request.POST.get('base_money'))
            range_up = float(request.POST.get('range_up'))
            range_up_count = int(request.POST.get('range_up_count'))
            range_down = float(request.POST.get('range_down'))
            range_down_count = int(request.POST.get('range_down_count'))
            range_total = int(request.POST.get('range_total'))
            rate_drop = float(request.POST.get('rate_drop'))
            count = int(request.POST.get('count'))
            target_up = float(request.POST.get('target_up'))
            target_down = float(request.POST.get('target_down'))

            # 1. 플러스 마이너스 로 기준이 되는 금액 선정
            base_moeny_range_up = base_money + int(round(base_money * (range_up/100),1))
            base_moeny_range_down = base_money - int(round(base_money * (range_down/100),1))
            
            result_lists = [] # 최종 리스트를 담을 리스트
            last_result = 0 # 최종 평균을 담을 변수

            for z in range(count):
            # 2. 랜덤하게 생성하여 원하는 수량만큼 생성해서 리스트에 넣는다
                base_money_range_up_list = random.sample(range(base_money,base_moeny_range_up),range_up_count)
                base_money_range_down_list = random.sample(range(base_moeny_range_down,base_money),range_down_count)
                print("+2.5",base_money_range_up_list)
                print("-2.5",base_money_range_down_list)
            # 3. 두 배열을 합친뒤 요청갯수만큼 최종 리스트 추출
                lists_total = base_money_range_up_list+base_money_range_down_list
                lists = random.sample(lists_total,range_total)
                print("전체 리스트 :",lists_total )
                print("4개 리스트 :",lists )
                list_money = 0
                for a in lists: #뽑은 최종리스트를 모두 더하기
                    list_money = list_money +  a
                list_money = list_money / range_total # 뽑은 최종 리스트를 모두 더한값의 평균
                print("4개평균값 : ",list_money)
                base_money_drop = int(round(list_money*(rate_drop/100),1)) #낙찰하한 계산
                print("낙찰하한 :",base_money_drop )
            # 4. 낙하하한값  보다 낮은값 삭제
                for a in lists:
                    if base_money_drop > a:
                        print("삭제됨 :" ,a)
                        lists.remove(a)

                result_lists.append(list_money)
            # 5. 낙하하한값과 가장 가까운값
                # np_list = np.asarray(lists)
                # idx = (np.abs(np_list - base_money_drop)).argmin() #  numpy를 이용한 배열에서 가장 가까운 값 찾기
                
                # result_lists.append(np_list[idx])

            last_result_lists = np.array(result_lists)
            last_result = int(np.mean(last_result_lists)) # 최종 평균
            last_result_limit = int(last_result*(rate_drop/100)) #최저낙찰값

            target_result_up = int(last_result*((rate_drop+target_up)/100))
            target_result_down = int(last_result*((rate_drop+target_down)/100))
            return render(
                request,
                "accounts/estimate_result.html",
                {
                    'nav_main':"회계",
                    'nav_sub_1':"적격심사견적",
                    'base_money' : base_money,
                    'range_up' : range_up,
                    'range_up_count' : range_up_count,
                    'range_down' : range_down,
                    'range_down_count' : range_down_count,
                    'range_total' : range_total,
                    'rate_drop' : rate_drop,
                    'count' : count,
                    'last_result': last_result,
                    'last_result_limit':last_result_limit,
                    'result_lists':result_lists,
                    'base_moeny_range_up':base_moeny_range_up,
                    'base_money_range_down':base_moeny_range_down,
                    'target_result_up':target_result_up,
                    'target_result_down':target_result_down,
                },
            )
        else:
            print("POST 오류")