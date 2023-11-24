from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm
from django.conf import settings


plt.rcParams['font.family'] = 'Malgun Gothic'  # 'Malgun Gothic'은 윈도우에서 기본적으로 제공하는 한글 폰트입니다.
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel("C:/Users/USER/data_semi_project/project/services_priority.xlsx")

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def data(request):
    return render(request, 'data.html')

def service1(request):
    if request.method == 'POST':
        # 사용자 입력 받아오기
        자치구 = request.POST.get('자치구')
        성별 = request.POST.get('성별').upper()
        try:
            연령대 = int(request.POST.get('연령대'))
        except ValueError:
            return HttpResponse("연령대는 숫자로 입력해주세요.")

        # 입력된 조건에 맞는 데이터를 찾기
        target_data = df[(df['자치구'] == 자치구) & (df['성별'] == 성별) & (df['연령대'] == 연령대)]
        
        if target_data.empty:  # 데이터가 없는 경우
            return HttpResponse("입력하신 자치구, 성별, 연령대에 해당하는 데이터가 없습니다.")

        # 서비스 우선순위 데이터만 선택
        service_data = target_data.iloc[:, 4:] # '성별' 제외
        
        # 순위와 함께 결과를 출력
        services = []
        for i, service in enumerate(service_data.values[0], 1):
            services.append(f"{i} {service}")
        
        return render(request, 'service1.html', {'services': services})
    else:
        return render(request, 'service1.html')

def service2(request):
    if request.method == 'POST':
        # 서비스와 파일명을 매칭
        service_files = {
            '배달 서비스': "C:/Users/USER/data_semi_project/project/service_target/delivery.xlsx",
            '금융 서비스': "C:/Users/USER/data_semi_project/project/service_target/finance.xlsx",
            '게임 서비스': "C:/Users/USER/data_semi_project/project/service_target/game.xlsx",
            '넷플릭스': "C:/Users/USER/data_semi_project/project/service_target/netflix.xlsx",
            '쇼핑 서비스': "C:/Users/USER/data_semi_project/project/service_target/shopping.xlsx",
            '유튜브': "C:/Users/USER/data_semi_project/project/service_target/youtube.xlsx",
            '동영상/방송 서비스': "C:/Users/USER/data_semi_project/project/service_target/video.xlsx"
        }

        # 사용자 입력 받아오기
        서비스 = request.POST.get('서비스')

        # 사용자가 입력한 서비스가 service_files에 존재하는지 확인
        if 서비스 not in service_files:
            return HttpResponse("입력하신 서비스는 존재하지 않습니다. 다시 입력해주세요.")

        # 파일이 존재하면 해당 파일을 불러옵니다.
        filename = os.path.join(settings.BASE_DIR, '..', 'service_target', service_files[서비스])
        print(f"Attempting to open file at: {filename}")  # Add this line
        df = pd.read_excel(filename)


        # 서비스 사용일수가 많은 순서대로 정렬
        sorted_target = df.groupby(['자치구', '성별', '연령대'])[f'{서비스} 사용일수'].mean().sort_values(ascending=False)
        
        target_services = df.iloc[:, 5:]

        # 상위 7개의 타겟을 추천
        recommended_targets = sorted_target[:7].index.tolist()

        # 순위와 함께 결과를 출력
        targets = []
        other_services = []
        for i, target in enumerate(recommended_targets, 1):
            targets.append(f"{i}순위: {target}")
        for i, service in enumerate(target_services, 1):
            other_services.append(f"{i}순위: {service}")

        return render(request, 'service2.html', {'targets': targets, 'other_services': other_services})
    else:
        return render(request, 'service2.html')