from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Liberian(models.Model):
    liberian = models.CharField(max_length = 15)
    tel = models.IntegerField()
    location = models.CharField(max_length = 30)
    date_registered = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.liberian
    
class Borrowed_Book(models.Model):
    name = models.ForeignKey(User,on_delete = models.CASCADE)
    liberian = models.ForeignKey(Liberian,on_delete= models.CASCADE)
    book_title = models.CharField(max_length = 20)
    date_borrowed = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name.username , 'borrowed' , self.book_title
    
