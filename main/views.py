from django.shortcuts import render, get_object_or_404
from main.models import Post

# Create your views here.
def main(request):
    post = Post.objects.all().order_by('-id')[:10]
    return render(request, 'main/main.html', {'posts': post})

def post_detail(request, post_id):
    posting = get_object_or_404(Post, pk=post_id)
    #get_object_or_404(클래스명, 검색조건{몇번 데이터, pk})
    #pk = primary key 객체들의 이름표, 구분자 데이터의 대표값
    #pk = pk에서 왼쪽은 현 객체의 pk이고 오른쪽 pk는 view에 지정한 객체
    return render(request, 'main/post_detail.html', {'post': posting})
 
def base(request):
    return render(request, 'main/base.html')