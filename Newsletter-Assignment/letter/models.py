from django.db import models

# Create your models here.


class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    #time = models.TimeField(auto_now_add=True)
    # dates will be automatically there

    def __str__(self):
        return self.email
# email is returned


class MailMessage(models.Model):
    title = models.CharField(max_length=120, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title
#title is returned