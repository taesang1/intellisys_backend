from django.shortcuts import HttpResponse, HttpResponseRedirect
from templates.db import DB
from templates.page import layout
from django.urls import reverse

db = DB()

def redirect(request):
  return HttpResponseRedirect(reverse('service'))

def del_button():
  return """<a style="border: solid 1px #c0c0c0;padding: 5px 7px;background-color: #e9e9e9;">삭제</a>"""

def service(request):
  head = ''
  row = ''
  title = f"""
  <h2 style='margin-bottom: 20px;'>Service메뉴 관리</h2>
  <div class="container" style="max-width: 100%;">
    <div class="row">
      <div class="col"> 총 갯수: {len(db.get_service())}</div>
      <div class="col" style="text-align: right; color:darkred;">
        * 한개라도 미노출시 "SERVICE" 메뉴 숨김처리됩니다
      </div>
    </div>
  </div>
  """
  for index, i in enumerate(db.get_service()):
    if index ==0:
      for j in i.keys():
        head += f'<th scope="col">{j}</th>'
      head +='<th scope="col">-</th>'
    row +=f"""
    <tr>
      <th scope="row" class="text-center">{i['serial']}</th>
      <td class="text-center">{'숨김'if i['imp'] == 0 else '노출'}</td>
      <td class="text-center">{i['seq']}</td>
      <td class="text-center">{i['pid']}</td>
      <td class="text-center">{i['title']}</td>
      <td class="text-center" style='width:80px'>{del_button()}</td>
    </tr>"""
  return html(request,table_body(row,head,title))

def service_case(request):
  head = ''
  row = ''
  title = f"""
  <h2 style='margin-bottom: 20px;'>Service 적용사례 조회</h2>
  <p>총 갯수 : {len(db.get_service_case())}</p>
  """
  for index, i in enumerate(db.get_service_case()):
    if index ==0:
      for j in i.keys():
        head += f'<th scope="col">{j}</th>'
      head +='<th scope="col">-</th>'
    row +=f"""
    <tr>
      <th scope="row" class="text-center">{i['serial']}</th>
      <td class="text-center">{'숨김'if i['imp'] == 0 else '노출'}</td>
      <td class="text-center">{i['title_11']}</td>
      <td class="text-center" style='width:80px'>{del_button()}</td>
    </tr>"""
  return html(request,table_body(row,head,title))

def questions(request):
  head = ''
  row = ''
  title = f"""
  <h2 style='margin-bottom: 20px;'>문의하기</h2>
  <p>총 갯수 : {len(db.get_questions())}</p>
  """
  for index, i in enumerate(db.get_questions()):
    if index ==0:
      for j in i.keys():
        head += f'<th scope="col">{j}</th>'
      head +='<th scope="col">-</th>'
    row +=f"""
    <tr>
      <th scope="row" class="text-center">{i['serial']}</th>
      <td class="text-center">{i['title']}</td>
      <td class="text-center">{i['name']}</td>
      <td class="text-center">{i['email']}</td>
      <td class="text-center">{i['regdate']}</td>
      <td class="text-center" style='width:80px'>{del_button()}</td>
    </tr>"""
  return html(request,table_body(row,head,title))

def blog_list(request):
  head = ''
  row = ''
  title = f"""
  <h2 style='margin-bottom: 20px;'>Blog 목록 조회</h2>
  <p>총 갯수 : {len(db.get_blog_list())}</p>
  """
  for index, i in enumerate(db.get_blog_list()):
    if index ==0:
      for j in i.keys():
        head += f'<th scope="col">{j}</th>'
      head +='<th scope="col">-</th>'
    row +=f"""
    <tr>
      <th scope="row" class="text-center">{i['serial']}</th>
      <td class="text-center">{i['title']}</td>
      <td class="text-center">{i['description']}</td>
      <td class="text-center">{i['publishedAt']}</td>
      <td class="text-center" style='width:120px;'>
      <a style="border: solid 1px #c0c0c0;padding: 5px 7px;background-color: #e9e9e9;">편집</a>
      {del_button()}
      </td>
    </tr>"""
  return html(request,table_body(row,head,title))

def table_body(row, head, title):
  text = f"""
  {title}
  <table class="table table-hover">
    <thead class="text-center">
      <tr style="color:white; background-color:rgba(78, 106, 134, 0.5);">
        {head}
      </tr>
    </thead>
    <tbody>
      {row}
    </tbody>
  </table>"""
  return text

def html(request, text):
  body = f"""
  <div style='height:100%; width: 100%'>
    {layout.head_layout()}
    <div class="row" style='height:100%'>
      <div class="col" style="max-width: 220px; border-right:1px solid #eceeef">
        {layout.left_layout()}
      </div>
      <div class="col">
        {text}
      </div>
    </div>
  </div>
  """
  return HttpResponse(body)
