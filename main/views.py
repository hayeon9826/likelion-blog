from django.shortcuts import render, get_object_or_404, redirect
from main.models import Post
from .forms import PostForm
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def main(request):
    post_list = Post.objects.all().order_by('-published_date')
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'main/main.html', {'posts': posts})

def post_detail(request, post_id):
    posting = get_object_or_404(Post, pk=post_id)
    #get_object_or_404(클래스명, 검색조건{몇번 데이터, pk})
    #pk = primary key 객체들의 이름표, 구분자 데이터의 대표값
    #pk = pk에서 왼쪽은 현 객체의 pk이고 오른쪽 pk는 view에 지정한 객체
    return render(request, 'main/post_detail.html', {'post': posting})
 
def base(request):
    return render(request, 'main/base.html')

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else: 
        form = PostForm()
    return render(request, 'main/post_new.html', {'form' : form})

def post_edit(request, post_id):
    if request.method == "POST":
        posting = get_object_or_404(Post, pk=post_id)
        form = PostForm(request.POST, instance = posting)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        posting = get_object_or_404(Post, pk=post_id)
        form = PostForm(instance = posting)
    return render(request, 'main/post_new.html', {'form' : form})

def post_remove(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('main')

