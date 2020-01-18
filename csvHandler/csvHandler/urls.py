"""csvHandler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from project.views import listone,listall,delete_city, index, listall_post,ApiEndpoint, get_login,get_signup,post_signup,post_login,post_logout,get_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', listone),
    path('', listall),
    path('finding', index, name = 'index'),
    #path('res', r_index, name = 'rindex')
    path('listall/post',listall_post, name = 'listall_post'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint

    path('login/', get_login),
    path('signup/', get_signup),
    path('signup/post', post_signup),
    path('login/post', post_login),
    path('logout/post',post_logout),
    path('logout',get_logout),
]
