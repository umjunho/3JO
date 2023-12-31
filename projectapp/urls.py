from django.urls import path
from . import views		

urlpatterns = [
    # http://127.0.0.1:8000/project/

    # 인덱스 페이지
    path('',views.index),
    path('index/',views.index),

    # 진단하기
    path('disease/',views.disease),
    # 진단 결과
    path('disease_result/',views.setFileInsert),
    # 마이 페이지
    path('mypage/',views.mypage),
    # 회원 정보 수정
    path('update_mypage/',views.update_mypage),

    #로그인
    path('login_chk/',views.login_chk),
    #로그아웃
    path('log_out/',views.logout_chk),
    # 회원 가입
    path('insert/',views.insert_user),
    # 아이디 찾기
    path('search_id/',views.search_id),
    # 비밀번호 찾기
    path('search_pw/',views.search_pw),
    # 아이디 중복 체크
    path('idChk/',views.idChk),

    # 자유 게시판 페이지
    path('board/',views.board),
    # 리뷰 게시판 페이지
    path('board_hospital/',views.board_hospital),
    # 자유 게시판 글쓰기 페이지
    path('inputpost/',views.inputpost),
    # 리뷰 게시판 글쓰기 페이지
    path('inputpost2/',views.inputpost2),
    # 게시글 작성
    path('post/',views.post),
    path('post2/',views.post2),
    # 게시판 상세조회
    path('board_view/',views.boardView),
    path('board_view2/',views.boardview2),
    # 게시판 수정 폼
    path('board_update_form/',views.boardUpdateForm),
    path('board_update_form2/',views.boardUpdateForm2),
    # 게시판 수정
    path('board_update/',views.boardUpdate),
    path('board_update2/',views.boardUpdate2),
    # 게시판 삭제
    path('board_delete/',views.boardDelete),
    path('board_delete2/',views.boardDelete2),
    # 댓글 삭제
    path('review_delete/',views.reviewDelete),
]
