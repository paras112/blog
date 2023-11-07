from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return(self.title)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return(self.content)


