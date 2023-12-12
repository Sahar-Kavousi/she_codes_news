from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='news_image', null=True, blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    story = models.ForeignKey(
        NewsStory,
        related_name="comments",
        on_delete=models.CASCADE
    )
    text = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
