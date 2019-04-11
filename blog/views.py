from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, UpdateView,
                                  DetailView, ListView, TemplateView)
from blog import models, forms
from django.utils import timezone

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostDetailView(DetailView):
    model = models.Post


class PostListView(ListView):
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published__lte=timezone.now()).order_by('-published')


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = '/'

    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = '/'

    model = models.Post
    form_class = forms.PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = models.Post
    success_url = reverse_lazy('blog:post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/'

    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(published__isnull=True).order_by('create_date')

#=====================================================================================================================

@login_required
def publish_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.publish()
    return redirect(reverse('blog:post_detail'), pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect(reverse('blog:post_detail'), pk=post.pk)

    else:
        form = forms.CommentForm()

    return render(request, 'blog/comment_form.html', {'form':form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment,pk=pk)

    comment.approve()
    return redirect(reverse('blog:post_detail'), pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)

    post_pk = comment.post.pk
    comment.delete()
    return redirect(reverse('blog:post_detail'), pk=post_pk)
