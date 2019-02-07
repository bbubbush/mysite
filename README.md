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
    >python manage.py startapp {app_name}
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
            #<BR>은 html에서 다음 줄로 이동하기 위해 쓰입니다.
            str += "{}기호 {}번 ({})<BR>".format(candidate.name, candidate.party_number, candidate.area) 
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

>Django의 경우 메모리에 올릴 때 모든 app의 template를 한곳에 모으기 때문에 중복과 충돌을 막기 위해 한번 더 app_name의 폴더를 만들어 경로를 분리

#### ~~Day 1 정리 끝~~

Day 2 (17/12/15)  
~ 여론조사 화면 구현

#### [ Template에 정보 채우기 ]
이전 강의가 하드코딩된 데이터로 정적인 페이지를 만들었다면 이번 강의는 DB에 저장된 데이터를 통해 동적인 페이지를 만듬

1. views.py에서 후보정보를 담아 html에 전달

    ```{.python}
    def index(request):
        candidates = Candidate.objects.all()
        context = {'candidates' : candidates} #context에 모든 후보에 대한 정보를 저장
        return render(request, 'elections/index.html', context) # context로 html에 모든 후보에 대한 정보를 전달
    ```
    - 항상 불러오고자 하는 테이블의 데이터는 import한 상태에서 진행

2. 위에서 넘겨준 데이터를 index.html에서 반복문으로 표현

    ```{.html}
    {% for candidate in candidates %}
    <tr>
        <td> {{ candidate.name }} </td>
        <td> {{ candidate.introduction }} </td>
        <td> {{ candidate.area }} </td>
        <td>기호 {{ candidate.party_number }} 번</td>
    </tr>
    {% endfor %}
    ```

#### [ MVC 패턴 ]
1. Model(데이터) - models.py
    - Candidate 클래스의 형식대로 데이터를 DB에 저장 및 호출

2. View(화면) - templates
    - 화면에 어떤 장면을 보여줄지를 결정

3. Controller(조율) - views.py
    - Candidate 모델에서 데이터를 읽어 index.html에 전달

>Django에서는 컨트롤러의 역할을 views.py에서 한다. 따라서 View를 담당한다고 혼동하기 쉽기 때문에 MTV라고 부르기도 한다. 

#### [ 여론조사 모델 ]
1. models.py에 Poll, Choice 클래스를 정의한다
2. 등록한 model을 admin을 통해 관리하기 위해 admin.py에 등록한다
3. models.py에는 들어가는 데이터의 형태에 대한 설계서이지 실제 DB에 만들어 진 것이 아니기 때문에 Power Shell에서 

>python manage.py makemigrations  
python manage.py migrate  

순으로 migrate 해야 한다

>여기서 고생이 많았는데 아무리 makemigrations를 해도 변화를 찾지 못해서이다. 처음엔 makemigrations 뒤에 app_name을 적어 해결되는 듯 했으나 그러면 0002의 새로운 파일이 생성되는 것이 아니라 0001의 Candidate 클래스가 만들어 진 곳에 오버라이드 되듯 덮어씌어졌다.
그래서 찾은 해결법이 다른 폴더에 새로운 프로젝트를 생성하고 아무런 정보가 기록되지 않은 db.sqlite3를 기존의 파일에 덮어쓰기해서 해결했다.

#### [ URL 다루기 ]
1. 링크를 걸 위치에 동적인 url을 삽입
    ```{.html}
    <td> <a href = "areas/{{candidate.area}}/">{{candidate.area}}</a> </td>
    ```

2. url에 대한 등록을 위해 urls.py에 정규표현식을 활용하여 패턴 추가
    ```{.python}
    urlpatterns = [
        url(r'^$', views.index),
        url(r'^areas/(?P<area>.+)/$', views.areas)
    ]
    ```
>이참에 정규표현식을 다시한번 복습하는 것도 좋을듯

#### [ 여론조사 화면 구현 ]
1. area에 따른 필터 결과를 html로 전달
    ```{.python}
    def areas(request, area):
        candidates = Candidate.objects.filter(area = area) #Candidate의 area와 매개변수 area가 같은 객체만 불러오기
        context = {'candidates': candidates,
        'area' : area}
        return render(request, 'elections/area.html', context)
    ```

2. 전달 받은 context를 for문으로 출력
    ```{.python}
    {% for candidate in candidates %}
    <tr>
        <td> {{candidate.name}}</td>
        <td> {{candidate.introduction}}</td>
        <td> 기호{{candidate.party_number}}번 </td>
        <td>
            <form action = "#" method = "post">
                <button name="choice" value="#">선택</button>
            </form>
        </td>
    </tr>
    {% endfor %}
    ```

3. area에 현재 진행 중인 poll이 있는지 확인
    ```{.python}
    def areas(request, area):
        today = datetime.datetime.now()
        try :
            poll = Poll.objects.get(area = area, start_date__lte = today, end_date__gte=today) # get에 인자로 조건을 전달해줍니다. 
            candidates = Candidate.objects.filter(area = area) # Candidate의 area와 매개변수 area가 같은 객체만 불러오기
        except:
            poll = None
            candidates = None
        context = {'candidates': candidates,
        'area' : area,
        'poll' : poll }
        return render(request, 'elections/area.html', context)
    ```

    - lte : less than equal  start_date__let = today (start_date <= today>)
    - gte : greater than equal  end_date__gte = today (today >=end_date)

4. html에 if를 사용해 결과가 있으면 표시하고 없으면 else를 이용해 없는 상태를 표시

    ```{.html}
    {% if poll %}
    ...
    {% else %}
    여론조사가 없습니다
    {% endif %}
    ```

**예외처리가 잘 되지 않는 경우 다음을 추가**

```{.python}
# C:\Code\mysite\settings.py
...
DATABASES = {
    #유지해주세요
}
DATABASE_OPTIONS = {'charset': 'utf8'} #추가
TIME_ZONE = 'Asia/Seoul' #추가
LANGUAGE_CODE = 'ko-kr' #추가
...
```
#### [ 여론조사 결과 저장 ]
1. 투표 결과를 DB에 저장
    - 해당 여론조사의 후보에게 투표할 경우 poll_id, cadidate_id 두 값을 가지고 투표 결과에 +1 시켜주면 된다
    - 기존의 값이 없다면 get으로 값을 가져올 때 예외가 발생하므로 예외처리로 값이 없는 상태일 때 값을 생성해 주는 코드를 작성한다

2. url.py에 url패턴 추가
    ```{.python}
    # C:\Code\mysite\elections\urls.py

    # 코드 유지

    urlpatterns = [
        # 기존 url 유지
        url(r'^polls/(?P<poll_id>\d+)/$', views.polls), #이 url에 대한 요청을 views.polls가 처리하게 만듭니다.
    ]
    ```

#### ~~Day 2 정리 끝~~

Day 3 (17/12/18)

#### [ 여론조사 결과보기1 - http redirect하기 ]
>HttpResponse가 바로 템플릿으로 이동한다면 HttpResponseRedirect는 views.py로 다시 이동한다 더 자세한 차이는 검색 고고

>jsp에서 게시판 수정이나 삭제 등은 처리가 된 후에 alert으로 간단한 메시지 표시 이후에 다시 홈으로 이동하게 처리했던 것과 비슷하다

#### [ 여론조사 결과보기2 - 후보 표시하기 ]
1. views.py에서 result함수를 통해 전달한 후보 데이터를 가져오기
    ```{.python}
    # C:\Code\mysite\elections\views.py

    def results(request, area):
        candidates = Candidate.objects.filter(area = area)
        polls = Poll.objects.filter(area = area)
        poll_results = []
        for poll in polls:
            result = {}
            result['start_date'] = poll.start_date
            result['end_date'] = poll.end_date

            poll_results.append(result)

        context = {'candidates':candidates, 'area':area,
        'poll_results' : poll_results}
        return render(request, 'elections/result.html', context)
    ```
2. result.html에 for문을 이용하여 가져온 데이터 표시하기
    - 간단한 작업이니 생략

#### [ 여론조사 결과보기3 - Dictionary로 데이터 정리하기 ]
1. 득표율을 구하는 비즈니스코드(핵심만 표시)
    ```{.python}
    # poll.id에 해당하는 전체 투표수
    total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
    result['total_votes'] = total_votes['votes__sum']

    rates = [] #지지율
    for candidate in candidates:
        # choice가 하나도 없는 경우 - 예외처리로 0을 append
        try:
            choice = Choice.objects.get(poll = poll, candidate = candidate)
            rates.append(
                round(choice.votes * 100 / result['total_votes'], 1)
                )
        except :
            rates.append(0)
    result['rates'] = rates
    poll_results.append(result)
    ```
    - 전체 표를 먼저 구한 후 각 후의 표를 가져와서 백분율로 표시

#### [ 404 오류 ]
1. HttpResponseNotFound로 예외처리
    ```{.python}
    def candidates(request, name):
        try :
            candidate = Candidate.objects.get(name = name)
        except:
            return HttpResponseNotFound("없는 페이지 입니다.")
        return HttpResponse(candidate.name)
    ```

2. Http404로 예외처리
    ```{.python}
    def candidates(request, name):
        try :
            candidate = Candidate.objects.get(name = name)
        except:
            raise Http404
        return HttpResponse(candidate.name)
    ```

3. get_object_or_404로 예외처리
    ```{.python}
    def candidates(request, name):
        candidate = get_object_or_404(Candidate, name = name)
        return HttpResponse(candidate.name)
    ```
>3개 모두 import를 해야 사용할 수 있으며 주소패턴을 벗어난 접근이나 주소패턴은 맞으나 views.py에 정의되지 않은 접근은 서로 다른 예외가 발생하므로 2번 혹은 3번을 통해 묶어서 처리할 수 있다.


#### [ 404페이지 변경하기 ]
1. 디버그 설정과 디렉토리 설정 바꿔주기
    - settings.py에서 DEBUG = False로 변경
    - ALLOWED_HOSTS = ['localhost'] 변경
    - TEMPLATES = [
        {
            ...
            'DIRS' : ['templates'],
            ...
        }
        ]
        추가

2. 404파일 만들어주기
    - root에 templates 폴더를 만들고 그 안에 404.html을 만들면 자동으로 404예외시 이 파일을 호출하여 보여준다

#### [ Template 상속 ]
공통된 html코드는 상속을 통해 뿌려줄 수 있다.

1. layout.html 설정
    - 공통된 html코드를 layout.html에 모아둔다
    - 변수로 활용되어야 하는 곳은 {% block 변수명 %}{% endblock %} 을 통해 지정한다

2. layout.html을 상속하기
    - 상속이 필요한 파일들은 맨 위에 {% extends 'elections/layout.html' %} 을 입력하여 상속

> 코드의 재사용성을 높이고 관리가 편하기 때문에 상속을 사용하여 template을 관리하는 것은 매우 유용

#### [ 네비게이션바 추가하기 ]
여기는 크게 특별한 부분은 없으나  urls.py파일에서 url 패턴에 name을 지정할 수 있다는 것을 알려준다

```{.python}
app_name = 'elections'
urlpatterns = [
    url(r'^$', views.index, name = 'home')
]
```

#### [ 파일 사용하기 ]
1. static폴더를 통해 파일을 관리
    - templates와 마찬가지로 app마다 가지고 있는 static을 하나로 합쳐서 관리하기 떄문에 static폴더 내에 app_name의 폴더를 하나 더 만들어서 관리해야 한다

2. template에서 static 내의 파일을 사용하기 위해선 {% load staticfiles %} 를 추가해야 한다

    - staic 파일의 주소값을 적을 땐 {% static '경로' %}를 사용


출처 : [장고를 활용한 웹사이트 만들기 with 정두식](https://programmers.co.kr/learn/courses/6)
