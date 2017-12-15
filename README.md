# mysite
Django를 활용한 웹페이지 만들기(with 정두식)

Day 1 (17/12/14)  
~ 템플릿으로 html 불러오기


#### <정리>

#### [ Django 설치하기 ]
>Python이 먼저 설치되어 있어야 하고 pip가 깔려있어야 한다
    pip install django

#### [ Django 프로젝트 만들기 ]
1. Django 프로젝트 생성
    - Power Shell으로 프로젝트를 만들 위치로 이동 후 

        django-admin startproject {project_name} 


2. Django 서버 실행
    - Power Shell으로 프로젝트 안으로 이동(manage.py가 있는 위치)

        python manage.py runserver port_number(생략시 8000)


3. Django 서버 접속
    - 127.0.0.1 혹은 localhost:8000
    - It Worked! 화면이 나오면 성공


4. Django 서버 중단
    - Power Shell에 ctrl + c 입력 시 서버 중지


Day 2 (17/12/14)  
~ 여론조사 화면 구현


https://programmers.co.kr/learn/courses/6
