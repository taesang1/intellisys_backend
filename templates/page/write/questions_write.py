from templates.page import list

def questions_write(request):
    text = """
    <div  style = 'width:50%'>
    <form action="/create/" method="post">
        <h3>Service 메뉴 정보</h3>
        <div class="row">
            <label for="frm_id" class="col-sm-2 col-form-label" style="color:red;">메뉴 ID</label>
            <div class="col" style="display: flex;">
                <input class="form-control" type="text" id="frm_id" name="m_id" value="" placeholder="페이지 ID를 입력해주세요.">
            </div>
            <div class="col">
                <span style='align-self: center;'>&nbsp; ( views/service/<span style='color:red;'>메뉴 ID</span>.ejs 파일 )</span>
            </div>
        </div>
        <div class="row">
            <label for="frm_title" class="col-sm-2 col-form-label">메뉴명</label>
            <div class="col-sm-10">
                <input class="form-control" type="text" id="frm_title" name="m_title" value="" placeholder="메뉴명을 입력해주세요.">
            </div>
        </div>
        <input type="hidden" id="frm_url" name="m_url" value="" >
        <div class="row">
            <label for="frm_title" class="col-sm-2 col-form-label">순번</label>
            <div class="col-sm-10">
                <input class="form-control" type="text" id="frm_title" name="m_seq" value="" placeholder="노출 순번 입력해주세요.">
            </div>
        </div>
        <div class="row">
            <label for="frm_title" class="col-form-label col-sm-2 pt-0">노출여부</label>
            <div class="col-sm-10">
                <div class="form-checkt">
                    <input id="m_imp" type="checkbox" name="m_imp" value="1">
                    <label for="m_imp">노출함</label>
                </div>
            </div>
        </div>
        <div class="row">
            <label class="col-form-label col-sm-2 pt-0"></label>
            <div class="col-sm-10">
                <div class="form-checkt">
                    <button>등록</button>
                </div>
            </div>
        </div> 
    </from>
    </div>"""
    return list.html(request,text)