from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('', PostListView.as_view)
    path('posts/<int:pk>')
    path('posts/new/')
    path('posts/<int:pk>/')
    path('posts/<int:pk>/')
]