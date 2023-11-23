from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64
import matplotlib.font_manager as fm

plt.rcParams['font.family'] = 'Malgun Gothic'  # 'Malgun Gothic'은 윈도우에서 기본적으로 제공하는 한글 폰트입니다.
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel("C:/Users/USER/data_semi_project/project/region_age_sex_services.xlsx")

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def data(request):
    return render(request, 'data.html')

def service1(request):
    # 사용자 입력 받아오기
    자치구 = request.POST.get('자치구')
    성별 = request.POST.get('성별')
    연령대 = request.POST.get('연령대')

    # 입력된 조건에 맞는 데이터를 찾기
    target_data = df[(df['자치구'] == 자치구) & (df['성별'] == 성별) & (df['연령대'] == 연령대)]

    # 서비스 사용일수 데이터만 선택
    service_data = target_data.iloc[:, 4:] # '성별' 제외
    
    # 사용일수가 많은 순서대로 정렬
    sorted_service = service_data.mean().sort_values(ascending=False)
    
    # 상위 7개의 서비스를 추천
    recommended_service = sorted_service.index[:7].tolist()
    
    # 서비스 이름에서 ' 사용일수'를 제거
    recommended_service = [service.split(' 사용')[0] for service in recommended_service]
    
    # 순위와 함께 결과를 출력 및 그래프 생성
    services = []
    values = []
    for i, (service, value) in enumerate(sorted_service[:7].items(), 1):
        service_name = service.split(' 사용')[0]
        services.append(f'{i}순위: {service_name}')  # 순위를 추가하여 출력
        values.append(value)

    # 그래프로 결과 나타내기
    plt.figure(figsize=(10, 6))
    bars = plt.barh([s.split(': ')[1] for s in services[::-1]], values[::-1])  # 그래프에는 순위를 제외한 서비스 이름만 표시
    plt.xlabel('평균 사용일수')
    plt.title('서비스 추천 순위')

    # 그래프 위에 수치 표시
    for bar in bars:
        width = bar.get_width()
        plt.text(width*1.01, bar.get_y() + bar.get_height()/2, f'{width:.2f}', va='center')

    # 그래프를 이미지로 변환
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()  # 그래프 닫기
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    
    return render(request, 'service1.html', {'services_values': zip(services, values), 'data': uri})

def service2(request):
    return render(request, 'service2.html')
