from django.db import models

# Create your models here.


class MyUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=255, unique=True, help_text="username")
    email = models.CharField(max_length=255, unique=True, help_text="email")
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True,
                             blank=True, help_text="Phone")
    fullname = models.CharField(
        max_length=255, null=True, blank=True, help_text="full name")

    def save(self):
        return super().save()
