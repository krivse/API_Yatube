from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Здесь должен быть заголовок')
    slug = models.SlugField(unique=True)
    description = models.TextField(
        verbose_name='Группа',
        help_text='Группа, '
        'к которой будет относиться пост')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name="posts", blank=True, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='following',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='follower',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ['user', 'following']