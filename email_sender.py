import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_username, smtp_password, recipient_email, message):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        server.sendmail(smtp_username, recipient_email, message)
        server.quit()

        print("Email sent successfully")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Failed to authenticate: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")