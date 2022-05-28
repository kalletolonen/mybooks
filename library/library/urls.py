from django.contrib import admin
from django.urls import path
from booksofmine import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>', views.BookDetailView.as_view()),
    path('books/<int:pk>/update', views.BookUpdateView.as_view()),
    path('books/new/', views.BookCreateView.as_view()),
    path('books/<int:pk>/delete', views.BookDeleteView.as_view()),
    path('authors/', views.AuthorListView.as_view()),
    path('authors/new/', views.AuthorCreateView.as_view()),
    path('authors/<int:pk>', views.AuthorDetailView.as_view()),
    path('authors/<int:pk>/update', views.AuthorUpdateView.as_view()),
    path('authors/<int:pk>/delete', views.AuthorDeleteView.as_view()),
    path('genres/', views.GenreListView.as_view()),
    path('genres/<int:pk>', views.GenreDetailView.as_view()),
    path('genres/<int:pk>/update', views.GenreUpdateView.as_view()),
    path('genres/<int:pk>/delete', views.GenreDeleteView.as_view()),
    path('genres/new/', views.GenreCreateView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
]
