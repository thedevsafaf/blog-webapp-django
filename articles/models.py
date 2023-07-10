from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
