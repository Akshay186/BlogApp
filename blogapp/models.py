from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        print(self.id)
        return reverse('home', )

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default="general")
    snippet = models.CharField(max_length=255, default="Add blog post snippet here, so that users understand what the post is about.")
    cover_image = models.ImageField(null=True, blank=True, upload_to="media/_/")
    body = RichTextField(blank="Write blog body here...", null=True)
    #body = models.TextField()
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name= "blog_posts" )

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        print(self.id)
        return reverse('article-detail', args=[str(self.id)])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

