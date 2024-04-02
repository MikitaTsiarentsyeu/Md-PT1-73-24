from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import Post, Author
from .forms import AddPost, AddPostModelForm
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

    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post_entry = form.save(commit=False)
            post_entry.issued = datetime.datetime.now()
            post_entry.author = Author.objects.all()[0]
            # post_entry.title = form.cleaned_data['title']
            # post_entry.content = form.cleaned_data['content']
            # post_entry.post_type = form.cleaned_data['post_type']
            # post_entry.image = form.cleaned_data['image']

            # post_entry.save()

            form.save_m2m()
            post_entry = form.save()

            return redirect('browse', post_entry.id)

    else:
        form = AddPostModelForm()

    return render(request, 'create.html', {'form':form})

# def create_post(request):

#     if request.method == "POST":
#         form = AddPost(request.POST, request.FILES)

#         if form.is_valid():
#             post_entry = Post()
#             post_entry.issued = datetime.datetime.now()
#             post_entry.author = Author.objects.all()[0]
#             post_entry.title = form.cleaned_data['title']
#             post_entry.content = form.cleaned_data['content']
#             post_entry.post_type = form.cleaned_data['post_type']
#             post_entry.image = form.cleaned_data['image']

#             post_entry.save()

#             return redirect('browse', post_entry.id)

#     else:
#         form = AddPost()

#     return render(request, 'create.html', {'form':form})