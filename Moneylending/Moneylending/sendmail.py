import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Moneylending.settings")
from django.core.mail import send_mail

print('mail sending')
send_mail('test', 'django', 'sd2009002@rediffmail.com', ['siddharth.dubey.1993@gmail.com'], fail_silently=False)
print('mail sent')
