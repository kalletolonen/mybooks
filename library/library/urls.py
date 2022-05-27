from django.contrib import admin
from django.urls import path
from booksofmine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>', views.BookDetailView.as_view()),
    path('books/<int:pk>/update', views.BookUpdateView.as_view()),
    path('books/new/', views.BookCreateView.as_view()),
    path('books/<int:pk>/delete', views.BookDeleteView.as_view()),
    path('authors/', views.AuthorListView.as_view()),
    
]
