from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to="posts/", verbose_name="Rasm")
    title = models.CharField(max_length=155, verbose_name="Sarlavha")
    description1 = models.TextField(verbose_name="Text 1")
    description2 = models.TextField(verbose_name="Text 2")
    paragraph = models.CharField(max_length=155, verbose_name="Mavzu")
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=155)
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.CharField(max_length=155)

    def __str__(self):
        return self.username


class Contact(models.Model):
    name = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=155)
    message = models.TextField()

    def __str__(self):
        return self.name

