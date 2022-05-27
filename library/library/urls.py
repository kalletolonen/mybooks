from django.contrib import admin
from django.urls import path
from booksofmine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view()),
]
