from django.db import models

class Account(models.Model):
    user_account    = models.CharField(max_length=50)
    password        = models.CharField(max_length=300)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_account'
