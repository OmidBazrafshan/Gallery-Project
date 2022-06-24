from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField( max_length=120)
    description = models.TextField()
    is_active = models.BooleanField()
    image=models.ImageField(upload_to="article-images")
    related_user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    related_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    related_user = models.ForeignKey(User ,  on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
class Gallery(models.Model):
    image=models.ImageField(upload_to="article-images")
    related_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    related_user = models.ForeignKey(User ,  on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url
    