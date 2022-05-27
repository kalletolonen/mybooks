from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=3000)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    def __str__(self):
            return f"{self.title}"

    def get_absolute_url(self):
        return f"/books/{self.pk}" 

            
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

    
