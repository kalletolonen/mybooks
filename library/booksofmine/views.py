from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class BookListView(ListView): 
	model = models.Book

