from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.TextField(max_length=50)
    def __str__(self):
        return self.name
class Smile(models.Model):
    name=models.CharField(max_length=50)
    age=models.TextField(max_length=50)
    def __str__(self):
        return self.name
class Business(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=50)
    def __str__(self):
        return self.name
class Twinkle(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=50)
    def __str__(self):
        return self.name
class kitty(models.Model):
    name=models.CharField(max_length=50)
    price=models.TextField(max_length=50)
    def __str__(self):
        return self.name
class Success(models.Model):
    name=models.CharField(max_length=50)
    price=models.TextField(max_length=50)
    def __str__(self):
        return self.name










    
