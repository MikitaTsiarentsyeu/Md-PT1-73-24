from django import forms
from .models import Post


class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label='Post title')
    content = forms.CharField(lable='Content', widget=forms.Textarea(attrs={'class':"content_text_area"}))
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label='Post type')
    image = forms.ImageField(label ='Main image')
