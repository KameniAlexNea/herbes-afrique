from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.


from .models import Post, PostImage
 
def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})
 
def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'blog/detail.html', {
        'post': post,
        'photos': photos
    })

class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now())

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'blog/post_detail.html', {'post':post})


'''def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts})'''


def post_new(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            return HttpResponseRedirect(reverse('blog:post_detail', args=(post.pk,)))
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method =="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            return HttpResponseRedirect(reverse('blog:post_detail', args=(post.pk,)))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})