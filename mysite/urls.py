"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from polls.views import HomepageView, AuthorsView, AuthorPostsView, SignUpView, post_details
from django.contrib.auth.views import (
            LoginView, 
            LogoutView, 
            PasswordResetView, 
            PasswordResetDoneView,
            PasswordResetConfirmView,
            PasswordResetCompleteView
        )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("homepage/", HomepageView.as_view(), name='homepage'),
    path("authors/", AuthorsView.as_view()),
    path("posts/<int:pk>", AuthorPostsView.as_view(), name='author_posts'),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("signup/", SignUpView.as_view(), name='signup'),
    path("post/<int:id>", post_details), 
]

if settings.DEBUG: # If in localhost 
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

