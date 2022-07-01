from templates.page import list

def service_case_write(request):
    text = """
    <div  style = 'width:50%'>
    <form action="/create/" method="post">
        <div class="row mb-3">
            <label for="title_11" class="col-sm-2 col-form-label" >타이틀1-1</label>
            <div class="col-sm-10">
				<!-- <input type="text" id="frm_id" name="m_id" value="" placeholder="페이지 ID를 입력해주세요." style="width:30em;"> -->
				<textarea class="form-control" id="title_11" name="title_11" placeholder="타이틀1-1 입력해주세요." style="width:30em;height:4em;"></textarea>
			</div>
        </div>
        <div class="row mb-3">
            <label for="title_12" class="col-sm-2 col-form-label" >타이틀1-2</label>
            <div class="col-sm-10">
				<input class="form-control" type="text" id="title_12" name="title_12" value="" placeholder="타이틀1-2 입력해주세요." style="width:30em;">
			</div>
        </div>
		<div class="row mb-3">
            <label for="description" class="col-sm-2 col-form-label" >설명</label>
            <div class="col-sm-10">
				<!-- <input type="text" id="frm_id" name="m_id" value="" placeholder="페이지 ID를 입력해주세요." style="width:30em;"> -->
				<textarea class="form-control" id="description" name="description" placeholder="설명을 입력해주세요." style="width:30em;height:4em;"></textarea>
			</div>
        </div>
		<div class="row mb-3">
            <label for="img" class="col-sm-2 col-form-label" >상세이미지</label>
            <div class="col-sm-10">
				<input class="form-control" type="file" id="img" name="img" value="" placeholder="이미지를 선택해주세요." style="width:30em;">
			</div>
        </div>
		<div class="row mb-3">
            <label for="frm_title" class="col-sm-2 col-form-label">노출여부</label>
            <div class="col-sm-10">
				<div class="checkbox pull-left">
					<input id="imp" type="checkbox" name="imp" value="1" checked>
					<label for="imp">노출함</label>
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