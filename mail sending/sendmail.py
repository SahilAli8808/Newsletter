import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, name):
    # Email configuration
    from_email = 'a-5014@kmclu.ac.in'
    password = 'jokfdrcqznjgcroh'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart('alternative')
    message['Subject'] = f'Thanks For Subscribing!🙌'
    message['From'] = from_email
    message['To'] = to_email

    # Load the HTML template file
    with open('template.html', 'r', encoding='utf-8') as file:
        template = file.read()

    # Replace placeholders in the template with the actual content
    template = template.replace('{{name}}', name)
    template = template.replace('{{body}}', body)

    # Create the HTML message part
    html_part = MIMEText(template, 'html')

    # Attach the HTML message part to the email
    message.attach(html_part)

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)

        # Send the email
        server.sendmail(from_email, to_email, message.as_string())
        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"An error occurred while sending the email to {to_email}: {str(e)}")

    finally:
        # Close the connection
        server.quit()


# Read email IDs and friend names from the CSV file
def send_emails_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if present

        for row in reader:
            email = row[0]
            name = row[1]
            subject = 'Thanks for Subscribing!✨'
            body = '''<p>Dear {{name}},</p>
                     <p>Thank you for subscribing to our newsletter. We are thrilled to have you on board!</p>
                     <p>Stay tuned for the latest tech news, updates, and exciting offers. We promise to keep you informed and inspired.</p>
                     <p>If you have any questions or need assistance, feel free to reach out to us. We're here to help!</p>
                     <p>Thanks again, and welcome to our newsletter community!</p>'''

            send_email(subject, body, email, name)


# Usage: Provide the path to the CSV file containing email IDs and friend names
csv_file_path = 'Subscribers.csv'
send_emails_from_csv(csv_file_path)
