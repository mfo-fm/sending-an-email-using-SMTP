import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email():
    # Email account credentials
    from_email = "olaniyanfarouqmo@gmail.com"
    password = "****"  # Use the generated app password
    to_email = "olaniyanfarouqmo@yahoo.com"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Daily Report - " + datetime.datetime.now().strftime("%Y-%m-%d")

    # Email body
    body = "This is your daily report."

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create server object with SSL option
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)
        
        # Send email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {to_email}.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
    send_email()
