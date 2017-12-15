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
    >python manage.py runserver port_number(생략시 8000, 이하 '서버실행'이란 말은 이 명령어를 의미)


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

#### **(중요)** [ mygrations와 DB ]
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
        python manage.py migrate

#### [ Django Admin ]
1. admin 계정 만들기
    - Power Shell로 project_name으로 이동 후 아래 명령어 입력 
    >python manage.py createsupersuer
    - 순서대로 ID, email(생략가능),PassWord, PassWord 입력 
    - 서버실행 후 브라우저에 아래 주소 입력
    >localhost:8000/admin
    - 위에서 만든 계정으로 로그인

2. Candidate 등록
    - app폴더의 admin.py에 model에서 정의한 Candidate를 등록
    ```{.python}
    #C\Code\mysite\elections\admin.py
    from django.contrib import admin
    from .models import Candidate

    admin.site.register(Candidate)
    ```
    - 브라우저를 새로고침 하면 Candidate가 반영
    - Candidate의 'Add Candidate'에서 내용을 추가하고 저장하면 object로 등록된 것을 확인 할 수 있음
    - 하지만 object로 표시되면 앞으로 데이터를 구분하기 힘들기 때문에 object 대신 후보의 이름이 나타나게 코드를 수정(models.py)
    ```{.python}
    #C\Code\mysite\elections\models.py
    from django.db import models

    class Candidate(models.Model):
        ...
        def __str__(self): 
            return self.name #object를 출력하면 name이 보입니다.
    ```
    - __str__ 메소드를 오버라이딩하여 원하는 문자열이 표시되도록 정의할 수 있다

#### [ 데이터 보여주기 ]
1. app_name 안에 있는 views.py를 아래와 같이 수정하여 데이터를 가져올 수 있다
    ```{.python}
    #C\Code\mysite\elections\views.py
    ...
    from .models import Candidate #models에 정의된 Candidate를 import 

    def index(request):
        candidates = Candidate.objects.all() #Candidate에 있는 모든 객체를 불러옵니다
        str = "" #마지막에 return해 줄 문자열입니다.
        for candidate in candidates:
            str += "{}기호 {}번 ({})<BR>".format(candidate.name, candidate.party_number, candidate.area) #<BR>은 html에서 다음 줄로 이동하기 위해 쓰입니다.
            str += candidate.introduction + "<P>" #<P>는 html에서 단락을 바꾸기 위해 쓰입니다.
        return HttpResponse(str)
    ```
    
#### [ Django shell을 통한 DB 제어 ]
별다른 필요성을 못느껴서 패스

단, 자주 사용되는 all(), get(), filter() 메소드는 기능과 문법을 익혀둘 것

#### [ Template으로 HTML 불러오기 ]
1. Template 추가하기
    - app폴더 안에 templates 폴더 생성(...\elections\templates))
    - templates폴더 아래 elecetions 폴더 생성(...\elections\templates\elections)
    - 가장 하위에 있는 elecetions안에 index.html 생성(...\elections\templates\elections\index.html)
    - 필요에 따라 index.html 과 views.py 수정
>Java의 MVC패턴과 비슷하다고 봐도 무방. Front와 Back의 분리





Day 2 (17/12/14)  
~ 여론조사 화면 구현


https://programmers.co.kr/learn/courses/6
