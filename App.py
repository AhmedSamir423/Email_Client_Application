import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from SendEmail import send_email
from ReceiveEmail import receive_email

# Initial Choice Window
def create_choice_window():
    choice_window = tk.Tk()
    choice_window.title("Email Client")
    choice_window.geometry("300x200")
    choice_window.configure(bg="#f0f0f0")
    choice_window.resizable(False, False)

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 14), background="#f0f0f0")
    style.configure("TButton", font=("Helvetica", 12, "bold"), padding=5)

    ttk.Label(choice_window, text="What would you like to do?").pack(pady=20)

    def on_send():
        choice_window.destroy()
        create_send_window()

    def on_receive():
        choice_window.destroy()
        create_receive_window()

    send_button = ttk.Button(choice_window, text="Send Email", command=on_send)
    send_button.pack(pady=10)

    receive_button = ttk.Button(choice_window, text="Receive Email", command=on_receive)
    receive_button.pack(pady=10)

    choice_window.mainloop()

# Full Send Email Window
def create_send_window():
    root = tk.Tk()
    root.title("Send Email - Email Client")
    root.geometry("600x700")
    root.configure(bg="#f0f0f0")

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
    style.configure("TButton", font=("Helvetica", 12, "bold"), padding=5)
    style.configure("TEntry", font=("Helvetica", 12))

    input_frame = ttk.Frame(root, padding=10)
    input_frame.pack(fill="x", pady=10)

    ttk.Label(input_frame, text="Sender Email:").grid(row=0, column=0, sticky="w", pady=5)
    sender_entry = ttk.Entry(input_frame, width=40)
    sender_entry.grid(row=0, column=1, padx=5)
    sender_entry.insert(0, "ahmedsamirelboridy@gmail.com")

    ttk.Label(input_frame, text="App Password:").grid(row=1, column=0, sticky="w", pady=5)
    password_entry = ttk.Entry(input_frame, width=40, show="*")
    password_entry.grid(row=1, column=1, padx=5)
    password_entry.insert(0, "wdgc ldat qzki amst")

    ttk.Label(input_frame, text="Recipient Email:").grid(row=2, column=0, sticky="w", pady=5)
    recipient_entry = ttk.Entry(input_frame, width=40)
    recipient_entry.grid(row=2, column=1, padx=5)
    recipient_entry.insert(0, "samarasamir4234@gmail.com")

    ttk.Label(input_frame, text="Subject:").grid(row=3, column=0, sticky="w", pady=5)
    subject_entry = ttk.Entry(input_frame, width=40)
    subject_entry.grid(row=3, column=1, padx=5)
    subject_entry.insert(0, "Test Email")

    ttk.Label(input_frame, text="Body:").grid(row=4, column=0, sticky="w", pady=5)
    body_text = scrolledtext.ScrolledText(input_frame, width=40, height=5, font=("Helvetica", 12))
    body_text.grid(row=4, column=1, padx=5)
    body_text.insert(tk.END, "This is a test email sent from my Python email client!")

    output_frame = ttk.Frame(root, padding=10)
    output_frame.pack(fill="both", expand=True)
    ttk.Label(output_frame, text="Output:", font=("Helvetica", 12, "bold")).pack(anchor="w")
    output_text = scrolledtext.ScrolledText(output_frame, width=70, height=20, font=("Courier", 11))
    output_text.pack(fill="both", expand=True)

    button_frame = ttk.Frame(root, padding=10)
    button_frame.pack(fill="x")

    def send_button_click():
        sender = sender_entry.get()
        password = password_entry.get()
        recipient = recipient_entry.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", tk.END).strip()
        if not all([sender, password, recipient, subject, body]):
            messagebox.showerror("Error", "All fields are required!")
            return
        send_email(sender, password, recipient, subject, body, output_text)

    send_button = ttk.Button(button_frame, text="Send Email", command=send_button_click)
    send_button.pack(side="left", padx=10)

    root.mainloop()

# Minimal Receive Email Window (Fixed)
def create_receive_window():
    root = tk.Tk()
    root.title("Receive Email - Email Client")
    root.geometry("400x500")
    root.configure(bg="#f0f0f0")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
    style.configure("TButton", font=("Helvetica", 12, "bold"), padding=5)
    style.configure("TEntry", font=("Helvetica", 12))

    # Input Frame
    input_frame = ttk.Frame(root, padding=10)
    input_frame.pack(fill="x", pady=10)

    ttk.Label(input_frame, text="Email Address:").grid(row=0, column=0, sticky="w", pady=5)
    email_entry = ttk.Entry(input_frame, width=30)
    email_entry.grid(row=0, column=1, padx=5)
    email_entry.insert(0, "samarasamir4234@gmail.com")

    ttk.Label(input_frame, text="App Password:").grid(row=1, column=0, sticky="w", pady=5)
    password_entry = ttk.Entry(input_frame, width=30, show="*")
    password_entry.grid(row=1, column=1, padx=5)
    password_entry.insert(0, "bxnq afdw ywfo uhon")

    # Button Frame (Moved up for better flow)
    button_frame = ttk.Frame(root, padding=10)
    button_frame.pack(fill="x", pady=5)

    def receive_button_click():
        email_user = email_entry.get()
        email_pass = password_entry.get()
        if not all([email_user, email_pass]):
            messagebox.showerror("Error", "Email and password are required!")
            return
        receive_email(email_user, email_pass, output_text)

    receive_button = ttk.Button(button_frame, text="Receive Latest Email", command=receive_button_click)
    receive_button.pack(side="left", padx=10)

    # Output Frame
    output_frame = ttk.Frame(root, padding=10)
    output_frame.pack(fill="both", expand=True)
    ttk.Label(output_frame, text="Latest Email:", font=("Helvetica", 12, "bold")).pack(anchor="w")
    output_text = scrolledtext.ScrolledText(output_frame, width=50, height=20, font=("Courier", 11))
    output_text.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    create_choice_window()