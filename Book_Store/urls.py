"""
URL configuration for Book_Store project.

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
from django.urls import path, include
from authors import views as a_view
from books import views as b_view
from information import views as i_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/',a_view.AuthorView.as_view()),
    path('author/<int:pk>/',a_view.AuthorById.as_view()),
    path('book/',b_view.BookView.as_view()),
    path('book/<int:pk>/',b_view.BookById.as_view()),
    path('leftover/', i_view.InformationView.as_view()),
    path('history/<int:pk>/', i_view.InformationHistoryView.as_view()),
    path('book_search/', b_view.BookSearchView.as_view(), name='book-search'),
    ]
