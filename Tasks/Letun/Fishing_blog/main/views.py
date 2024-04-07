from django.shortcuts import render
import datetime
from .models import Post, Author
from .forms import AddPost
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.http import HttpResponseNotFound, Http404

def test(request):
    now = datetime.datetime.now()
    return render(request, 'test.html', {"my_time":now})


def pattern_view(request, param):
    print(param, type(param))
    now = datetime.datetime.now()
    return render(request, 'test.html', {"my_time":now})

def posts(request):
    posts = Post.objects.all()

def browse_post(request, post_url_id):
    request.POST
    try:
       p = Post.objects.get(id=post_url_id)
    except ObjectDoesNotExist:
        #return HttpResponseNotFound("cannot find post specified")
        raise Http404("cannot find post specified")
    print(p.title, type(p))
    now = datetime.datetime.now()
    return render(request, 'browse_post.html', {'post':p})


def create_post(request):
    form = AddPost() 
    return render(request, 'create.html', {'form':form}) 