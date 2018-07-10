"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from app_posts import views as post_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.NewView.as_view()),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^api/users/$', post_views.UserList.as_view()),
    url(r'^api/categories/$', post_views.CategoryList.as_view()),
    url(r'^api/categories/(?P<pk>[0-9a-f\-]+)/$', post_views.CategoryDetail.as_view()),
    url(r'^api/posts/$', post_views.PostList.as_view()),
    url(r'^api/posts/(?P<pk>[0-9a-f\-]+)/$', post_views.PostDetail.as_view()),

]


