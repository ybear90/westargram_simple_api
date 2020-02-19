from django.db import models

# Create your models here.
class Account(models.Model):
    username    = models.CharField(max_length=50)
    email       = models.CharField(max_length=50)
    password    = models.CharField(max_length=300)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'

class Comment(models.Model):
    comment_user    = models.CharField(max_length=50)
    comments        = models.CharField(max_length=500)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
