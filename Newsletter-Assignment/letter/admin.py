from django.contrib import admin
from . models import MailMessage, Subscribers
#import mail messages and subscribers from the current models

# Register your models here.
admin.site.register(MailMessage)
admin.site.register(Subscribers)
