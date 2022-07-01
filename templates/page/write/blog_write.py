from templates.page import list

def blog_write(request):
    text = """
        <div  style = 'width:50%'>
        <form action="/create/" method="post">
            <div class="mb-3">
                <label for="title" class="form-label">제목</label>
                <input type="text" class="form-control" id="title" name="title" placeholder="제목을 입력 해주세요">
            </div>

            <div class="mb-3">
                <div class="sources-container" style="position: relative">
                    <label for="links" class="form-label">원문 링크</label>
                    <input type="text" class="form-control" id="links" name="links" placeholder="원문 링크를 입력 해주세요">
                    <button id="sources-plus">+</button>
                </div>
            </div>

            <div class="mb-3" style="width: 34em">
                <label for="publishedAt" class="form-label">작성일</label>
                <div class="col-sm-10">
                    <input type="date" class="form-control" id="date" name="publishedAt"max="9999-12-31" maxlength='10'>
                </div>
            </div>

            <div class="mb-3" style="width: 50em">
                <label for="tumnailImg" class="form-label">썸네일 이미지</label>
                <div class="col-sm-10">
                    <input type="file" class="form-control" id="tumnailImg" name="tumnailImg">
                </div>
            </div>

            <div class="mb-3" style="width: 50em">
                <label for="titleImg" class="form-label">본문 이미지</label>
                <div class="col-sm-10">
                    <input type="file" class="form-control" id="titleImg" name="titleImg">
                </div>
            </div>

            <div class="mb-3">
                <label for="tumnailTxt" class="form-label">썸네일 텍스트</label>
                <input type="text" class="form-control" id="tumnailTxt" name="tumnailTxt" placeholder="썸네일 텍스트를 입력 해주세요">
            </div>

            <div class="mb-3">
                <label for="description" class="form-label">요약</label>
                <input type="text" class="form-control" id="description" name="description" placeholder="요약글을 입력 해주세요">
            </div>

            <div class="mb-3">
                <label for="text" class="form-label">내용 작성</label>
                <textarea class="form-control" placeholder="내용을 입력해 주세요" id="text" rows="2"></textarea>
            </div>

            <button>등록</button>
        </from>
    </div>"""
    return list.html(request,text)