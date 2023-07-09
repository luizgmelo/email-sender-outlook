import smtplib

import email.message 

# Create message
msg = email.message.Message()
msg['From'] = str(input("E-mail Sender: "))
password = str(input("Sender Password: "))
msg['To'] = str(input("E-mail Recipient: "))
msg['Subject'] = str(input("Subject: "))
msg.add_header('Content-Type', 'text/html')
body_email = str(input("Message: "))
msg.set_payload(body_email)

# Send the message via SMTP server
s = smtplib.SMTP('smtp-mail.outlook.com', 587)
s.starttls()
s.login(msg['From'], password)
s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
print("Email successfully sent")
s.quit()





