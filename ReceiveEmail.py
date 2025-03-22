import imaplib
import email
from email.header import decode_header

def receive_email(email_user, email_pass):
    imap_server = "imap.gmail.com"
    imap_port = 993  # SSL port for Gmail

    try:
        # Connect to the IMAP server with SSL
        print(f"Connecting to {imap_server}:{imap_port}")
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        print("Connected to IMAP server successfully.")

        # Login to Gmail
        mail.login(email_user, email_pass)
        print("Logged in successfully.")

        # Select the inbox
        mail.select("inbox")
        print("Inbox selected.")

        # Search for all emails in the inbox
        status, messages = mail.search(None, "ALL")
        if status != "OK":
            raise Exception("Failed to search emails.")

        # Get the list of email IDs
        email_ids = messages[0].split()
        if not email_ids:
            print("No emails found in inbox.")
            return

        # Fetch the latest email (last ID in the list)
        latest_email_id = email_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        if status != "OK":
            raise Exception("Failed to fetch email.")

        # Parse the raw email
        raw_email = msg_data[0][1]
        email_message = email.message_from_bytes(raw_email)

        # Extract and decode subject
        subject, encoding = decode_header(email_message["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")
        print(f"Subject: {subject}")

        # Extract sender
        from_ = email_message.get("From")
        print(f"From: {from_}")

        # Extract body
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                    print("Body:")
                    print(body)
                    break
        else:
            body = email_message.get_payload(decode=True).decode("utf-8", errors="ignore")
            print("Body:")
            print(body)

    except Exception as e:
        print(f"Failed to receive email: {str(e)}")

    finally:
        if 'mail' in locals():
            mail.logout()
            print("Logged out from IMAP server.")

# Test the function
if __name__ == "__main__":
    email_user = "samarasamir4234@gmail.com"  # Your Gmail
    email_pass = "dybc jdsy reff gfuc"  # Your App Password
    
    receive_email(email_user, email_pass)