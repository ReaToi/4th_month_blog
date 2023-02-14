from django.shortcuts import render
from posts.models import Post

# Create your views here.


def main_page_vief(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def possts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=context)


