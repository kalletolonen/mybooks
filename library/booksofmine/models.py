from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=3000)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey('Genre', null=True,on_delete=models.SET_NULL)

    def __str__(self):
            return f"{self.title}"

    def get_absolute_url(self):
        return f"/books/{self.pk}" 

class BookInstance(models.Model):
    def get_duedate():
        return datetime.today() + timedelta(days=30)

    user = models.ForeignKey('auth.User',null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey('Book', null=True,on_delete=models.SET_NULL)
    loan_date = models.DateField(null=True, blank=True, default=datetime.today)
    due_back = models.DateField(null=True, blank=True, default=get_duedate)
    LOAN_STATUS = (
            ('o', 'On loan'),
            ('a', 'Available'),
            ('r', 'Reserved'),
        )
    status = models.CharField(
            max_length=1,
            choices=LOAN_STATUS,
            blank=True,
            default='o',
            help_text='Book availability',
        )
           
class Author(models.Model):
    name = models.CharField(max_length=300, default="")
    country = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
                return f"{self.pk}. {self.name}"        

    def get_absolute_url(self):
        return f"/authors/{self.pk}" 

class Genre(models.Model):
    genre = models.CharField(max_length=300, unique=True)
    
    def __str__(self):
        return f"{self.genre}"     

    def get_absolute_url(self):
        return f"/genres/{self.pk}" 
