from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='Gallery/imags')
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

class Books(models.Model):
    image = models.ImageField(upload_to='Books/imags')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    about = models.TextField()
    data = models.CharField(max_length=12)
    pages = models.CharField(max_length=10)

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)