import imaplib
import email
from email.header import decode_header

def receive_email(email_user, email_pass, output_text):
    imap_server = "imap.gmail.com"
    imap_port = 993

    mail = None
    try:
        output_text.delete(1.0, 'end')  # Clear previous output
        output_text.insert('end', f"Connecting to {imap_server}:{imap_port}\n")
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        output_text.insert('end', "Connected to IMAP server successfully.\n")

        mail.login(email_user, email_pass)
        output_text.insert('end', "Logged in successfully.\n")

        mail.select("inbox")
        output_text.insert('end', "Inbox selected.\n")

        status, messages = mail.search(None, "ALL")
        if status != "OK":
            raise Exception("Failed to search emails.")

        email_ids = messages[0].split()
        if not email_ids:
            output_text.insert('end', "No emails found in inbox.\n")
            return

        latest_email_id = email_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        if status != "OK":
            raise Exception("Failed to fetch email.")

        raw_email = msg_data[0][1]
        email_message = email.message_from_bytes(raw_email)

        subject, encoding = decode_header(email_message["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")
        output_text.insert('end', f"Subject: {subject}\n")

        from_ = email_message.get("From")
        output_text.insert('end', f"From: {from_}\n")

        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                    output_text.insert('end', "Body:\n")
                    output_text.insert('end', f"{body}\n")
                    break
        else:
            body = email_message.get_payload(decode=True).decode("utf-8", errors="ignore")
            output_text.insert('end', "Body:\n")
            output_text.insert('end', f"{body}\n")

    except Exception as e:
        output_text.insert('end', f"Failed to receive email: {str(e)}\n")

    finally:
        if mail is not None:
            mail.logout()
            output_text.insert('end', "Logged out from IMAP server.\n")

if __name__ == "__main__":
    email_user = "samarasamir4234@gmail.com"
    email_pass = "bxnq afdw ywfo uhon"
