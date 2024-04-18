from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import Post, Author
from .forms import AddPost, AddPostModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, Http404
from django.contrib.auth.decorators import permission_required

from django.views import View

def test(request):
    now = datetime.datetime.now()
    return render(request, 'test.html', {"my_time":now})

def pattern_view(request, param):
    print(param, type(param))
    now = datetime.datetime.now()
    return render(request, 'test.html', {"my_time":now})

class PostModelViewBase:

    model = Post

    def get_all_posts(self):
        return self.model.objects.all()
    
    def get_post(self, id):
        try:
            return self.model.objects.get(id=id)
        except:
            return False
        
    def add_post(self, form, author):
        try:
            post_entry = form.save(commit=False)
            post_entry.issued = datetime.datetime.now()
            post_entry.author = author

            form.save_m2m()
            post_entry = form.save()
            return post_entry
        except:
            return False


class SessionViewBase:

    session_key = 'viewed'

    def get_post_id_from_session(self, request):
        return request.session.get(self.session_key, [])

    def set_post_post_id_for_session(self, request, id):
        viewed_posts = request.session.get(self.session_key, [])
        if id not in viewed_posts:
            viewed_posts.append(id)
            request.session[self.session_key] = viewed_posts


class PostsView(PostModelViewBase, SessionViewBase, View):

    template = 'posts.html'

    def get(self, request):
        posts = self.get_all_posts()
        viewed_posts = self.get_post_id_from_session(request)
        return render(request, self.template, {'posts':posts, 'viewed_posts': viewed_posts})


class PostsView(PostModelViewBase, SessionViewBase, View):

    template = 'posts.html'

    def get(self, request):
        posts = self.get_all_posts()
        vp = self.get_post_id_from_session(request)
        return render(request, self.template, {'posts':posts, 'vp': vp})

class PostView(PostModelViewBase, SessionViewBase, View):

    template = 'browse_post.html'

    def get(self, request, post_url_id):
        p = self.get_post(post_url_id)
        if p:
            self.set_post_post_id_for_session(request, post_url_id)

        return render(request, self.template, {'post':p, 'id':post_url_id})
    
class CreatePostView(PostModelViewBase, SessionViewBase, View):

    template = 'create.html'
    form = AddPostModelForm

    def render_form(self, request, form):
        return render(request, self.template, {'form':form})

    def get(self, request):
        return self.render_form(request, self.form())

    def post(self, request):
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            author = Author.objects.get(email=request.user.email)
            post_entry = self.add_post(form, author)
            if post_entry:
                return redirect('browse', post_entry.id)

        return self.render_form(request, form)























def posts(request):
    posts = Post.objects.all()
    
    vp = request.session.get('viewed', [])

    # posts_list = ''

    # for post in posts:
    #     posts_list += f"<li><p>{post.title}</p></li>"

    # response = f"<h1>All posts</h1><ul>{posts_list}</ul>"

    # return HttpResponse(response)

    return render(request, 'posts.html', {"posts":posts, "vp":vp})

def browse_post(request, post_url_id):
    try:
        p = Post.objects.get(id=post_url_id)
        vp = request.session.get('viewed', [])
        if post_url_id not in vp:
            vp.append(post_url_id)
        request.session['viewed'] = vp
    except ObjectDoesNotExist:
        # return HttpResponseNotFound("cannot find post specified")
        raise Http404("cannot find post specified")
    
    return render(request, 'browse_post.html', {'post':p})

@permission_required('main.post.can_edit')
def create_post(request):

    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post_entry = form.save(commit=False)
            post_entry.issued = datetime.datetime.now()
            post_entry.author = Author.objects.get(email=request.user.email)
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