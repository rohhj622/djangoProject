# djangoProject

*django framework 를 사용하여 만든 여러가지 프로젝트, 
Django 한그릇 뚝딱을 참고하여 진행합니다*

### 1. to_do_list
> db : sqlite3
- 모든 할 일 열람 select * --> isDone = False(0) 이면 열람, 할 일  insert, 완료 시 delete --> isDone = True(1) update
- CRD 기능을 갖춤
- app을 여러개로 두는 이유 : 유지보수를 위함
- get, post에 따라 request.GET, request.POST 달라짐
- 20.8.21

### 2. RestaurantShare
> db : sqlite3
- app을 생성하면 잊지말고 setting.py에 추가하기 : 그렇지 않으면 templates 파일을 읽지 못 함.
