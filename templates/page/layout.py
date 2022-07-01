def head_layout():
  head_menu = '''
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <div class="container" style="max-width: 100%;">
      <div class="row" style="background-color: #f9f2f2; padding: 5px;">
        <div class="col" style="color: #010050;">
        IntelliSys ADMIN
        </div>
        <div class="col" style="text-align: right;">
          <a style="text-decoration: none; color:#010050;">로그아웃</a>
        </div>
      </div>
      <div class="row" style="padding: 5px; border-bottom:1px solid #eceeef">
        &nbsp
      </div>
    </div>
    '''
  return head_menu

def left_layout():
  menu_list = [
    ['Service메뉴 관리', '등록'],
    ['Service적용사례 관리', '등록'],
    ['문의하기 관리', '폼 관리'],
    ['Blog 관리', '작성']
  ]
  menu = ''
  list_page_link = {
    'Service메뉴 관리':['/service_list/','/service_write/'],
    'Service적용사례 관리':['/service_case/','/service_case_write/'],
    '문의하기 관리':['/questions/','/questions_write/'],
    'Blog 관리':['/blog_list/','/blog_write/']
  }
  for i in menu_list:
    menu += f"""
    <li>
      <a href='{list_page_link[i[0]][0]}'>
        <span>{i[0]}</span>
      </a>
      <ul>
        <li>
          <a href='{list_page_link[i[0]][0]}'>
          <span>조회</span></a>
        </li>
        <li>
          <a href='{list_page_link[i[0]][1]}'><span>{i[1]}</span></a>
        </li>
      </ul>
    </li>
    """
  left_menu = f"""
  <ul>
    {menu}
  </ul>
  """+"""
  <style>
    ul, li{
      list-style:none;
      padding: 5px 10px;
    }
    a {
    text-decoration: none;
    color: black;
    }
  </style>"""
  return left_menu