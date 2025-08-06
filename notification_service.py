import smtplib
from email.message import EmailMessage

# Send email notification to user
def send_email(to_email, subject, body):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = "noreply@complaints.ai"
        msg['To'] = to_email
        msg.set_content(body)

        # Localhost SMTP server or replace with Gmail/SendGrid config
        with smtplib.SMTP('localhost', 1025) as smtp:
            smtp.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print("Error sending email:", e)

# Stub for SMS (you can integrate with Twilio, etc.)
def send_sms(phone_number, message):
    print(f"SMS to {phone_number}: {message}")
