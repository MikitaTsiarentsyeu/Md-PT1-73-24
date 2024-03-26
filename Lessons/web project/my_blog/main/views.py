from django.shortcuts import render
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
    pass

def browse_post(request, post_url_id):
    try:
        p = Post.objects.get(id=post_url_id)
    except ObjectDoesNotExist:
        # return HttpResponseNotFound("cannot find post specified")
        raise Http404("cannot find post specified")
    print(p.title, type(p))
    now = datetime.datetime.now()
    return render(request, 'test.html', {"my_time":now})

def create_post(request):
    pass