# 초기 세팅
장고 설치
python -m pip install Django

# DB 세팅
templates 폴더 안에 .env 파일을 만들어 db 정보를 입력한다(host, user, password, db)

# 실행 방법 
명령어 입력 : python manage.py runserver

* RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods

위 에러가 발생하다면 모듈 추가 설치

pip install cryptography
