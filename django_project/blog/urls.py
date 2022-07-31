from django.urls import path

from . import views
from .views import (PostCreateView, PostDeleteView, PostDetailView,
                    PostEditView, PostListView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
