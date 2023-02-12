from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def register(response):

	if response.method == "POST":
		form = RegisterForm(response.POST)
		username = str(response.POST['username'])
		email = str(response.POST['email'])
		if form.is_valid():
			sendGreetingMessage(username, email)
			form.save()
			return redirect("/success")
	else:
		form = RegisterForm()

	return render(response, "register/register.html", {"form": form})


def sendGreetingMessage(username, email):
	template = render_to_string('email_template.html', {'name': username}) 
	email = EmailMessage('Registraton successful ' + str(username) + '!',
    	template,
    	settings.EMAIL_HOST_USER,
    	[str(email)]
    	)
	email.fail_silently = False
	email.send()
    


