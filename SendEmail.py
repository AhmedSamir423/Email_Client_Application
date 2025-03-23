import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body, output_text):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = None
    try:
        output_text.delete(1.0, 'end')  # Clear previous output
        output_text.insert('end', f"Resolving hostname: {smtp_server}\n")
        ip_address = socket.gethostbyname(smtp_server)
        output_text.insert('end', f"Resolved {smtp_server} to IP: {ip_address}\n")

        output_text.insert('end', f"Connecting to {smtp_server}:{smtp_port}\n")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        output_text.insert('end', "Connected to SMTP server successfully.\n")

        server.login(sender_email, sender_password)
        output_text.insert('end', "Logged in successfully.\n")

        server.send_message(msg)
        output_text.insert('end', f"Email sent successfully to {recipient_email}\n")

    except socket.gaierror as e:
        output_text.insert('end', f"DNS resolution failed for {smtp_server}: {str(e)}\n")
    except smtplib.SMTPAuthenticationError:
        output_text.insert('end', "Authentication failed! Check your credentials.\n")
    except Exception as e:
        output_text.insert('end', f"Failed to send email: {str(e)}\n")

    finally:
        if server is not None:
            server.quit()
            output_text.insert('end', "Connection closed.\n")


if __name__ == "__main__":
    sender = "ahmedsamirelboridy@gmail.com"
    password = "wdgc ldat qzki amst"
    recipient = "samarasamir4234@gmail.com"
    subject = "Test Email"
    body = "This is a test email sent from my Python email client!"
    