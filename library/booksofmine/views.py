from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class BookListView(ListView): 
	model = models.Book

class BookDetailView(DetailView): 
	model = models.Book

class BookUpdateView(UpdateView): 
	model = models.Book
	fields = "__all__"
	success_url = "/books"

class BookCreateView(CreateView): 
	model = models.Book
	fields = "__all__"
	success_url = "/books"

