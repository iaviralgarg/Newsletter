from django import forms
from . models import Subscribers, MailMessage
# importing subscribers and mail messages form the current model

class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'
        #we need everything in this case so fields is all, title and message (in forms.py)
