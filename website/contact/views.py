from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.
def contact(request):
	title = 'Contact Us'
	form = contactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		comment = request.POST['comment']
		subject1 = "Message from St. Augustine's Catholic Church Website"
		message_content= f"Name: {name}\nEmail: {email}\nSubject: {subject}\n \n \nComment:\n{comment}"
		message = '%s' %(message_content)
		emailFrom = request.POST['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject1, message, emailFrom, emailTo, fail_silently=True )
		title = 'Thanks'
		confirm_message = 'Thanks for the message. We will get back to you shortly.'
		form = None

	context = {'title': title, 'form': form, 'confirm_message': confirm_message,}
	template = 'contact/contact-us.html'
	return render(request,template,context)




def email_list(request):
	email = request.POST['email']
	subject1 = "New Email from St. Augustine's Catholic Church Website"
	message_content= f"Email: {email}"
	message = '%s' %(message_content)
	emailFrom = request.POST['email']
	emailTo = [settings.EMAIL_HOST_USER]
	send_mail(subject1, message, emailFrom, emailTo, fail_silently=True )
	title = 'Thanks'
	confirm_message = 'Thanks for the message. We will get back to you shortly.'
	form = None

	context = {'confirm_message': confirm_message,}
	template = 'home/home.html'
	return render(request,template,context)
