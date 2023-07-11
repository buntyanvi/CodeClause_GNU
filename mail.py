import tkinter as tk
from tkinter import messagebox
import smtplib

def send_email():
    sender_email = sender_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end")

    try:
        _extracted_from_send_email_9(subject, message, sender_email, receiver_email)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")


# TODO Rename this here and in `send_email`
def _extracted_from_send_email_9(subject, message, sender_email, receiver_email):
    # SMTP server and port for the email provider
    smtp_server = "smtp.example.com"
    smtp_port = 587

    # Your email credentials
    email_username = "your-email@example.com"
    email_password = "your-email-password"

    # Create an SMTP connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_username, email_password)

    # Construct the email message
    email_message = f"Subject: {subject}\n\n{message}"

    # Send the email
    server.sendmail(sender_email, receiver_email, email_message)
    server.quit()

    messagebox.showinfo("Success", "Email sent successfully!")

# Create the main application window
window = tk.Tk()
window.title("Mail Application")
window.geometry("400x300")
window.config(bg="#f5f5f5")

# Header Label
header_label = tk.Label(window, text="Mail Application", font=("Arial", 16), bg="#f5f5f5")
header_label.pack(pady=10)

# Frame for Input Fields
input_frame = tk.Frame(window, bg="#f5f5f5")
input_frame.pack(pady=10)

# Sender Email
sender_label = tk.Label(input_frame, text="Sender Email:", font=("Arial", 12), bg="#f5f5f5")
sender_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
sender_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
sender_entry.grid(row=0, column=1, padx=10, pady=5)

# Receiver Email
receiver_label = tk.Label(input_frame, text="Receiver Email:", font=("Arial", 12), bg="#f5f5f5")
receiver_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
receiver_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
receiver_entry.grid(row=1, column=1, padx=10, pady=5)

# Subject
subject_label = tk.Label(input_frame, text="Subject:", font=("Arial", 12), bg="#f5f5f5")
subject_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
subject_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
subject_entry.grid(row=2, column=1, padx=10, pady=5)

# Message
message_label = tk.Label(input_frame, text="Message:", font=("Arial", 12), bg="#f5f5f5")
message_label.grid(row=3, column=0, padx=10, pady=5, sticky="nw")
message_text = tk.Text(input_frame, font=("Arial", 12), width=30, height=5)
message_text.grid(row=3, column=1, padx=10, pady=5)

# Send Button
send_button = tk.Button(window, text="Send Email", font=("Arial", 12), command=send_email)
send_button.pack(pady=10)

# Run the application
window.mainloop()
