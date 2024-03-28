from django.shortcuts import render, HttpResponse
import datetime
from .models import Post, Author
from django.core.exceptions import ObjectDoesNotExist
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

    # posts_list = ''

    # for post in posts:
    #     posts_list += f"<li><p>{post.title}</p></li>"

    # response = f"<h1>All posts</h1><ul>{posts_list}</ul>"

    # return HttpResponse(response)

    return render(request, 'posts.html', {"posts":posts})

def browse_post(request, post_url_id):
    try:
        p = Post.objects.get(id=post_url_id)
    except ObjectDoesNotExist:
        # return HttpResponseNotFound("cannot find post specified")
        raise Http404("cannot find post specified")
    
    return render(request, 'browse_post.html', {'post':p})

def create_post(request):
    pass