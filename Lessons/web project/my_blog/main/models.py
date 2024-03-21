from django.db import models


class Author(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(primary_key=True)

class Post(models.Model):

    POST_TYPES = [('c', "copyright"), ('a', "marketing")]

    title = models.CharField(max_length=100)
    content = models.TextField()
    issued = models.DateTimeField()
    post_type = models.CharField(choices=POST_TYPES, max_length=1)
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)