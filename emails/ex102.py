import smtplib

gmail_user = 'username'  
gmail_password = 'password'

sent_from = gmail_user  
to = ['test@example.com', 'test@example.com']  
subject = 'Testing email'  
body = "Hey, what's up?\n\n- You"

email_text = """  
From: {}  
To: {}  
Subject: {}

{}
""".format(sent_from, ", ".join(to), subject, body)

message = "Subject: {}\n\n{}".format(subject, email_text)

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

print(smtpObj.ehlo())

smtpObj.starttls()

smtpObj.login(gmail_user, gmail_password)

smtpObj.sendmail(sent_from, to, message)

smtpObj.quit()