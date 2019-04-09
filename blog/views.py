from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, UpdateView,
                                  DetailView, ListView)
from blog import models

# Create your views here.
class PostDetailView(DetailView):
    model = models.Post


class PostListView(ListView):
    model = models.Post


class PostCreateView(CreateView):
    model = models.Post


class PostUpdateView(UpdateView):
    model = models.Post


class PostDeleteView(DeleteView):
    model = models.Post