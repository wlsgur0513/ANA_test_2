from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.core.paginator import Paginator
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pybo.models import Question
# Create your views here.zip()

def page(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    planning = Question.objects.order_by('-create_date')
    if kw:
        planning = planning.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(planning, 4)  # 페이지당 4개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'planning': page_obj, 'page': page, 'kw': kw}
    return render(request, 'page/planning.html', context)