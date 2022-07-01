import pymysql
from dotenv import load_dotenv
import os
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse

# load .env
load_dotenv(verbose=True)

class DB():
    def __init__(self) -> None:
        self.con = pymysql.connect(host=os.getenv('host'), user=os.getenv('user'), password=os.getenv('password'),
            db=os.getenv('db'), charset='utf8') #env파일에서 db정보를 읽어 연결한다
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)

    def close(self):
        self.con.close()

    def get_service(self):
        self.cur.execute('SELECT serial,imp,seq,pid,title FROM mnu_service order by serial asc;')
        rows = [data for data in self.cur.fetchall()]
        return rows
   
    def get_service_case(self):
        self.cur.execute('SELECT serial, imp, title_11 FROM mnu_service_case order by serial asc;')
        rows = [data for data in self.cur.fetchall()]
        return rows

    def get_questions(self):
        self.cur.execute("SELECT serial, title, name, email, from_unixtime(regdate, '%Y-%m-%d') as regdate FROM questions order by serial DESC;")
        rows = [data for data in self.cur.fetchall()]
        return rows

    def get_blog_list(self):
        self.cur.execute('SELECT serial,title,description,publishedAt FROM intellisys1.press ORDER BY publishedAt desc;')
        rows = [data for data in self.cur.fetchall()]
        return rows

    @csrf_exempt
    def create(request):
        return HttpResponse('ad')
    