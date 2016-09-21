#phoneTroubleshooting
A python-based phone troubleshooting application, that checks for intersections between user queries and arrays dependant on the required scenario. Then, if possible provide a potential solution to the issue and use an SMTP Server module to send the technician details regarding your case.
##Setup Process
In order to setup your Python script you need to alter the support.py module file with your SMTP server information. If you do not have access to an SMTP server, do not fear as you can make a free GMail account which will allow the script to work with full functionality.

In the script you will need to alter the following code:
```
SMTPserver = 'SET SMTP SERVER ADDRESS'
sender = user_email
destination = ['SET DESTINATION EMAIL ADDRESS']

USERNAME = "SET USERNAME"
PASSWORD = "SET PASSWORD"
```
If you wish to use GMail you may use these settings as a template:
```
SMTPserver = 'smtp.gmail.com'
sender = user_email
destination = ['TECHNICIAN EMAIL ADDRESS']

USERNAME = "GMAIL_USERNAME@gmail.com"
PASSWORD = "GMAIL_PASSWORD"
```
Once you have made this small tweak your Phone Troubleshooting application will be ready to go with a few demo brands and potential solutions.
