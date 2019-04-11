from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    re_path(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    re_path(r'^post/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(), name='post_update'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.publish_post, name='publish_post'),
    re_path(r'^post/(?P<pk>\d+)/delete/$', views.PostUpdateView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='draft_list'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
