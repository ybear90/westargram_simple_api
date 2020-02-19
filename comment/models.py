from django.db import models

class Comment(models.Model):
    user_account    = models.CharField(max_length=50)
    comments        = models.CharField(max_length=700)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_comment'