from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(ListView): 
	model = models.Book

class BookDetailView(DetailView): 
	model = models.Book

class BookUpdateView(LoginRequiredMixin, UpdateView): 
	model = models.Book
	fields = "__all__"
	success_url = "/books"
	login_url = '/accounts/login/'

class BookCreateView(CreateView): 
	model = models.Book
	fields = "__all__"
	success_url = "/books"
	login_url = '/accounts/login/'

class BookDeleteView(DeleteView): 
	model = models.Book
	success_url = "/books"
	login_url = '/accounts/login/'

class AuthorListView(ListView): 
	model = models.Author

class AuthorCreateView(CreateView): 
	model = models.Author
	fields = "__all__"
	success_url = "/books"
	login_url = '/accounts/login/'

class AuthorDetailView(DetailView): 
	model = models.Author

class AuthorUpdateView(UpdateView): 
	model = models.Author
	fields = "__all__"
	success_url = "/books"
	login_url = '/accounts/login/'

class AuthorDeleteView(DeleteView): 
	model = models.Author
	success_url = "/books"
	login_url = '/accounts/login/'

class GenreListView(ListView): 
	model = models.Genre

class GenreDetailView(DetailView): 
	model = models.Genre

class GenreUpdateView(UpdateView): 
	model = models.Genre
	fields = "__all__"
	success_url = "/genres"
	login_url = '/accounts/login/'

class GenreCreateView(CreateView): 
	model = models.Genre
	fields = "__all__"
	success_url = "/genres"
	login_url = '/accounts/login/'

class GenreDeleteView(DeleteView): 
	model = models.Genre
	success_url = "/genres"
	login_url = '/accounts/login/'
