from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	if request.method == 'POST':
		message_name=request.POST["message-name"]
		message_email=request.POST["message-email"]
		message_phone=request.POST["message-phone"]
		message=request.POST["message"]
		return render(request,"home.html",{'message_name':message_name})
		#send mail
		send_mail(message_name, message, message_email, ['oussamabouarfa2001@gmail.com'], )

	else:
		return render(request,"home.html",{})

def booking(request):
	return render(request,"booking.html",{})

    
