from django.core.mail import EmailMessage
import os


class Util:
  @staticmethod
  def send_mail (data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email=os.getenv('EMAIL_HOST_USER'),
      to=[data['to_email']] 
    )
    
    
    
    email.send()