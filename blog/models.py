from django.db import models
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = HTMLField('Текст записи')
    pub_date = models.DateTimeField('Дата публикации')
    articles = models.Manager()

    def __str__(self):
        return self.title

    def getCommentsCount(self):
        comments = models.Count(Comment)
        return comments


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField("Текст комментария")
    pub_date = models.DateTimeField('Дата добавления комментария')

