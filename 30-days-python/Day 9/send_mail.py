import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


username = 'waldiceiabarbalho@gmail.com'
password = 'senha!!'


def send_mail(text='Email Body', subject='Hello World', from_email='Waldiceia Barbalho <waldiceiabarbalho@gmail.com>', to_emails=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_emails
    msg['Subject'] = subject
    
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText("<h1>This is working</h1>", 'html')
    #msg.attach(html_part)

    msg_str = msg.as_string
    # login to my smtp server
    server = smtplib.SMTP('smtp.gmail.com', port=547)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()
    # with smtplib.SMTP() as server:
    #    server.login()
    #    pass
