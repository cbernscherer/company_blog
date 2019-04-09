from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list_view'),
    re_path(r'^post_detail/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail_view'),
]
