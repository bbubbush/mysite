# mysite
Django를 활용한 웹페이지 만들기(with 정두식)

Day 1 (17/12/14)  
~ 템플릿으로 html 불러오기


#### <정리>

#### [ Django 설치하기 ]
Python이 먼저 설치되어 있어야 하고 pip가 깔려있어야 한다

>pip install django

#### [ Django 프로젝트 만들기 ]
1. Django 프로젝트 생성
    - Power Shell으로 프로젝트를 만들 위치로 이동 후 
    >django-admin startproject {project_name} 


2. Django 서버 실행
    - Power Shell으로 프로젝트 안으로 이동(manage.py가 있는 위치)
    >python manage.py runserver port_number(생략시 8000)


3. Django 서버 접속
    - 127.0.0.1 혹은 localhost:8000
    - It Worked! 화면이 나오면 성공


4. Django 서버 중단
    - Power Shell에 ctrl + c 입력 시 서버 중지


#### [ Hello World 출력하기(app 만들기) ]

1. app 만들기
    - Power Shell으로 프로젝트 안으로 이동(manage.py가 있는 위치)
    >python manage.py startapp {app_name
    - 아무런 변화가 없지만 dir을 치면 app_name의 폴더가 생성되어 있음

2. index 함수 만들기
    - Power Shell으로 앱 안으로 이동(app_name을 elections로 만들었으므로 elections로 이동)
    - views.py(\프로젝트이름\앱이름\views.py) 수정 - 페이지 요청에 대해 hello world라는 httpResponse를 리턴

        ```{.python}
        #C\Code\mysite\elections\views.py  
        from django.shortcuts import render  
        from django.http import HttpResponse 

        def index(request):  
            return HttpResponse("Hello world")
        ```
3. app에 접근할 조건을 지정하는 함수 만들기
    - \프로젝트명\프로젝트명\urls.py에 urlpatterns 수정

4. 앞에서 생성한 index함수를 실행할 조건을 지정하는 함수 만들기
    - 앞서 생성한 {app_name}폴더로 이동
    - urls.py 파일 생성(app_name 폴더 안에 만들어야 함)
    - urls.py에 urlpatterns로 index 함수를 지정

#### [ 모델 클래스 ]
1. app과 관련된 정보를 저장
    - app_name 폴더 안에 있는 models.py에 정의
    - 모델 class는 models.Model을 상속 받아야 함(아래 코드 참조)
    >Tip.  Django에서 보통 model이름은 대문자로 시작하며, 단수형으로 사용
        ```{.python}
        # C:\Code\mysite\elections\models.py

        class Candidate(models.Model):
            name = models.CharField(max_length=10)
            introduction = models.TextField()
            area = models.CharField(max_length=15)
            party_number = models.IntegerField(default=1)
        ```

#### [ mygrations와 DB ]
1. 모델을 DB에 저장하기 위한 준비 과정
    - project_name 안에 있는 settings.py 안에 있는 INSTALLED_APPS 리스트에 elections(앱이름) 추가
    ```{.python}
    #C\Code\mysite\mysite\settings.py
    ...
    INSTALLED_APPS = [
        ...,
        '{app_name}' #추가
    ]
    ...
    ```
    - Power Shell로 project_name으로 이동 후 아래 명령어를 순서대로 입력
    >python manage.py makemigrations
    >python manage.py migrate



Day 2 (17/12/14)  
~ 여론조사 화면 구현


https://programmers.co.kr/learn/courses/6
