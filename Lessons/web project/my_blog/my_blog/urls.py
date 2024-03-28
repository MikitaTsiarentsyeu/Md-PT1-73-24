"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as main_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/test/', main_views.test),
    # path('main/<int:param>', main_views.pattern_view),
    # path('main/<str:param>', main_views.pattern_view),
    path('', main_views.posts, name='landing'),
    path('posts/', main_views.posts),
    path('posts/create', main_views.create_post, name='create'),
    path('posts/<int:post_url_id>', main_views.browse_post, name='browse'),
    # path('wiki/<str:pub_name>', main_views.browse_post, name='browse'),
]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)