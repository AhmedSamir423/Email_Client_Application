import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Use 465 if using SMTP_SSL

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = None
    try:
        print(f"Resolving hostname: {smtp_server}")
        ip_address = socket.gethostbyname(smtp_server)
        print(f"Resolved {smtp_server} to IP: {ip_address}")

        print(f"Connecting to {smtp_server}:{smtp_port}")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade to secure connection
        print("Connected to SMTP server successfully.")

        server.login(sender_email, sender_password)
        print("Logged in successfully.")

        server.send_message(msg)
        print(f"Email sent successfully to {recipient_email}")

    except socket.gaierror as e:
        print(f"DNS resolution failed for {smtp_server}: {str(e)}")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed! Make sure you enabled 'Less Secure Apps' or used an App Password.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

    finally:
        if server is not None:
            server.quit()
            print("Connection closed.")

# Test the function
if __name__ == "__main__":
    sender = "ahmedsamirelboridy@gmail.com"  # Replace with your Gmail
    password = "wdgc ldat qzki amst"   # Replace with your generated App Password
    recipient = "samarasamir4234@gmail.com"  # Replace with recipient email
    subject = "Test Email"
    body = "This is a test email sent from my Python email client!"

    send_email(sender, password, recipient, subject, body)
