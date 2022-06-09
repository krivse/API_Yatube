from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Group, Comment, Follow
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from .permissions import IsFollowingPermission


class PostViewSet(viewsets.ModelViewSet):
    """GET, POST - получаем список всех постов или создаём новый пост
    Доступно только авторизованному пользователю / на чтение."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """POST - пост записи."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """GET, PUT, PATCH - автор получает или редактирует по id."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        """DELETE - автор удаляет пост по id."""
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """GET - получение списка групп / информации о группе по id."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None


class CommentViewSet(viewsets.ModelViewSet):
    """GET - получение списка комментариев / комментариев по id."""
    serializer_class = CommentSerializer
    pagination_class = None

    def get_queryset(self):
        """GET - получаем список комментариев поста или создаём новый."""
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        """POST - пост записи."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        """GET, PUT, PATCH - автор получает или редактирует по id."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """DELETE - автор удаляет коммент по id."""
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        instance.delete()


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated|IsFollowingPermission]
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    search_fields_fields = ('follower',)

    def get_queryset(self):
        """GET - получение списка подписчиков."""
        return Follow.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        """POST - подписка на пользователя."""
        serializer.save(user=self.request.user)
