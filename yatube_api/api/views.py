
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post
from .permissions import AuthorOrIsAuthenticatedAndReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer)
from .viewsets import YatubeApiV1BaseViewSet


class PostViewSet(YatubeApiV1BaseViewSet):
    """Viewset for Posts."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for Groups."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(YatubeApiV1BaseViewSet):
    """Viewset for Comments."""
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Return comments which connected only with post."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        new_queryset = Comment.objects.filter(post=post.id)
        return new_queryset


class FollowViewSet(viewsets.ModelViewSet):
    """Viewset for Follow."""
    serializer_class = FollowSerializer
    permission_classes = [AuthorOrIsAuthenticatedAndReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Return objects which connected only with request user."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Set user from request as default user."""
        serializer.save(user=self.request.user)
