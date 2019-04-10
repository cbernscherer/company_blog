from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.author.username, self.title)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail_view', kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=64)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post_list_view')