from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Post, Author
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.utils.decorators import decorator_from_middleware
from django.utils import timezone
from datetime import datetime
class IndexView(generic.ListView):	
    template_name = 'home/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.order_by('-date')
class DetailsView(generic.DetailView):
    model = Post
    template_name = 'home/details.html'
class EditView(generic.UpdateView):
    model = Post
    fields = ('title', 'desc')
    template_name = 'home/edit.html'
    url = "/{id}"
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.title = request.POST.get("title")
        post.desc = request.POST.get("desc")
        post.save()
        return HttpResponseRedirect(reverse('blog:details', args=[post.id]))
class AuthorView(generic.DetailView):
    model = Author
    template_name = 'home/author.html'

class CreateView(generic.CreateView):
    model = Post
    fields = ('title', 'desc')
    template_name = 'home/create.html'
    def post(self, request):
        title1 = request.POST.get("title")
        desc1 = request.POST.get("desc")
        author1 = Author.objects.first()
        post = Post.objects.create(title=title1, date=datetime.now(), desc = desc1, author = author1)
        post_list = Post.objects.order_by('-date')
        return HttpResponseRedirect(reverse('blog:home', args=[]))


def index(request):
    post_list = Post.objects.order_by('-date')
    template = loader.get_template('home/index.html')
    context = {'post_list':post_list,}
    return HttpResponse(template.render(context, request))
def create(request):
    author = Author.objects[:1]
    template = loader.get_template('home/create.html')
    context = {'author':author,}
    return HttpResponse(template.render(context, request))

def author(request):
    author = Author.objects[:1]
    template = loader.get_template('home/author.html')
    context = {'author':author,}
    return HttpResponse(template.render(context, request))
def details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template = loader.get_template('home/details.html')
    context = {'post':post,}
    return HttpResponse(template.render(context, request))
def edit(request, post_id):
    template = loader.get_template('home/edit.html')
    post = get_object_or_404(Post, pk=post_id)
    context = {'post':post,}
    return HttpResponse(template.render(context, request))