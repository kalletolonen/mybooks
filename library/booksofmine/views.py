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

class BookCreateView(LoginRequiredMixin, CreateView): 
	model = models.Book
	fields = "__all__"
	success_url = "/books"
	login_url = '/accounts/login/'

class BookDeleteView(LoginRequiredMixin, DeleteView): 
	model = models.Book
	success_url = "/books"
	login_url = '/accounts/login/'

class AuthorListView(ListView): 
	model = models.Author

class AuthorCreateView(LoginRequiredMixin, CreateView): 
	model = models.Author
	fields = "__all__"
	success_url = "/books"
	login_url = '/accounts/login/'

class AuthorDetailView(DetailView): 
	model = models.Author

class AuthorUpdateView(LoginRequiredMixin, UpdateView): 
	model = models.Author
	fields = "__all__"
	success_url = "/books"
	login_url = '/accounts/login/'

class AuthorDeleteView(LoginRequiredMixin, DeleteView): 
	model = models.Author
	success_url = "/books"
	login_url = '/accounts/login/'

class GenreListView(ListView): 
	model = models.Genre

class GenreDetailView(DetailView): 
	model = models.Genre

class GenreUpdateView(LoginRequiredMixin, UpdateView): 
	model = models.Genre
	fields = "__all__"
	success_url = "/genres"
	login_url = '/accounts/login/'

class GenreCreateView(LoginRequiredMixin, CreateView): 
	model = models.Genre
	fields = "__all__"
	success_url = "/genres"
	login_url = '/accounts/login/'

class GenreDeleteView(LoginRequiredMixin, DeleteView): 
	model = models.Genre
	success_url = "/genres"
	login_url = '/accounts/login/'
