from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    username = models.CharField(max_length=300, blank=False, null=False)
    phone_number= models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField("Create time", auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.id} || {self.name} || {self.phone_number}"


class Post(models.Model):
    title = models.CharField(max_length=300)
    body  = models.TextField()
    url_name = models.URLField(max_length=400)
    address = models.CharField(max_length=400)
    create  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}  || {self.body}"