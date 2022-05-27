from django.shortcuts import render, redirect
# also importing redirect
from . forms import SubscibersForm, MailMessageForm
# from forms.py we are importing subscirbers form and mail messages form

from . models import Subscribers
#suscribers imported from current model
from django.contrib import messages
# messages is imported to know that we have successfully gotten the email of the subscriber
from django.core.mail import send_mail
#send mail function for sending mails back and forth
from django_pandas.io import read_frame
# to propoerly manipulate our data we import read frame

# Create your views here.


def index(request):
    if request.method == 'POST':
        #form method used is POST to keep it more secure, so we are using an if statement to make it more logical
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription to the newsletter is Successful')
            # this tells that we have gotten the email id succcessfully
            return redirect('/')
        #grabbing whatever they are entering and giving it to the forms and then saving it
    
    else:
        form = SubscibersForm()
    context = {
        'form': form,
    }
    return render(request, 'letter/index.html', context)


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    #  emails contains all the email of the subscribers and then those emails are read and fed to the dataframe we created named df and then from the dataframe df, mail list is reading the value of emails and displaying them
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message sent to the Mailing List')
            return redirect('mail-letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'letter/mail_letter.html', context)
