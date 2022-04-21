from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    author = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_date']


class Comment(models.Model):
    text = models.TextField(blank=False)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="add")

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_date').all()

    def __str__(self):
        return self.text[:15]







