import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email account credentials
sender_email = "dharakpandadiya@gmail.com"
receiver_email = "dharakjobs091@gmail.com"
password = "Godfather@5304#"

# Define email content
message = MIMEMultipart("alternative")
message["Subject"] = "Test Email"
message["From"] = sender_email
message["To"] = receiver_email

# Email body
text = """\
Hi,
This is a tset email sent using Python's smtplib.
"""

# Attach the body to the email
part1 = MIMEText(text, "plain")
message.attach(part1)

# Send the email using Gmail's SMTP server
try:
    # Connect to the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()  # Identify yourself to the server
    server.starttls()  # Secure the connection with TLS
    server.ehlo()  # Re-identify yourself after TLS

    # Log in to the server
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Terminate the connection
    server.quit()