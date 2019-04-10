from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, UpdateView,
                                  DetailView, ListView, TemplateView)
from blog import models, forms
from django.utils import timezone

# Create your views here.
class LoginView(TemplateView):
    template_name = 'about.html'

class AboutView(TemplateView):
    template_name = 'about.html'


class PostDetailView(DetailView):
    model = models.Post


class PostListView(ListView):
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published__lte=timezone.now).order_by('-published')


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse('blog:login')
    redirect_field_name = reverse('blog:post_detail')

    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse('blog:login')
    redirect_field_name = reverse('blog:post_detail')

    model = models.Post
    form_class = forms.PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse('blog:login')

    model = models.Post
    success_url = reverse_lazy('blog:post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = reverse('blog:login')
    redirect_field_name = reverse('blog:post_detail')

    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published__isnull=True).order_by('create_date')