from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label='Post title')
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'class':"content_text_area"}))
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label='Post type')
    image = forms.ImageField(label='Main image')

    def clean_title(self):

        raw_data = self.cleaned_data['title']
        # raw_content = self.cleaned_data['content'] error
        if raw_data == "test title":
            raise ValidationError("do not name it 'test title'!")
        
        cleaned_data = raw_data.strip()

        return cleaned_data
    
    def clean_content(self):

        title_data = self.cleaned_data.get('title', '')
        content_data = self.cleaned_data['content']

        if title_data == content_data:
            raise ValidationError("do not copy title to content!")
        
        return content_data



class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_type', 'image')
        labels = {'title':"Title", 'content':"Content"}

    def clean_title(self):

        raw_data = self.cleaned_data['title']
        # raw_content = self.cleaned_data['content'] error
        if raw_data == "test title":
            raise ValidationError("do not name it 'test title'!")
        
        cleaned_data = raw_data.strip()

        return cleaned_data