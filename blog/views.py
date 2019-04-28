from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html',
                  {'post_list': qs})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    all_tag = Tag.objects.all()
    mystr = post.tagged()
    my_tag = {}
    for t in all_tag:
        # mystr에서 t.name을 발견한 위치를 my_tag 사전에 등록
        # 키는 t.name으로, 값은 (못 찾으면 -1, 찾으면 양수)
        my_tag[t.name] = str(mystr).find(t.name)
    return render(request, 'blog/post_detail.html',
                  {'post': post, 'my_tag': my_tag})
