from turtle import title
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255) #criando variavel string / CharField
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Criando Variavel para o nome do Autor
    body = models.TextField() #textfield = Maior que string
    created = models.DateTimeField(auto_now_add=True) # data create
    update = models.DateTimeField(auto_now=True) #Data update post

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ("blog:detail", kwargs={"slug": self.slug})