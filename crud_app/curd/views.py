from django.shortcuts import render
from learning.models import Post

# Create your views here.


def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post(title=title, content=content)
        post.save()
    return render(request, 'new_post.html')


def get_post(request):
    post = Post.objects.all()
    return render(request, 'get_post.html', {'posts': post})