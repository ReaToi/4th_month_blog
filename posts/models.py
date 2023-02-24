from django.db import models

# Create your models here.


class Hashtag(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Post(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField(default=0.0)
    create_date = models.DateField(auto_now_add=True)
    modefied_date = models.DateField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=355)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    create_date = models.DateField(auto_now_add=True)
