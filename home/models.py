from django.db import models

# Create your models here.

class BookList(models.Model):
    BookId = models.AutoField(primary_key=True,unique=True)
    BookName = models.CharField(max_length=50)
    BookWriter = models.CharField(max_length=50)
    BookDisc = models.TextField()
    BookStatus = models.CharField(max_length=50 ,default="AVAILABLE")
