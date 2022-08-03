from django.shortcuts import redirect, render
from learning.models import Post
from django.contrib import messages

# Create your views here.

# post request
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post(title=title, content=content)
        post.save()
    return render(request, 'new_post.html')

# get request
def get_post(request):
    post = Post.objects.all()
    return render(request, 'get_post.html', {'posts': post})

# update request
def get_single_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        post.title = title
        post.content = content
        post.save()
    return render(request, 'edit.html', {'posts': post})

# delete request
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    messages.info(request, "Deleted")
    return redirect('/')