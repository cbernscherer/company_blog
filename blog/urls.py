from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('list/', views.PostListView.as_view(), name='post_list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('about/', views.AboutView.as_view(), name='about'),
    re_path(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    re_path(r'^post/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(), name='post_update'),
    re_path(r'^post/(?P<pk>\d+)/delete/$', views.PostUpdateView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='draft_list'),
]
