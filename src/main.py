from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import random
import smtplib

os.environ["mailpassword"]="qkert kp jgzk qwe hflx"
os.environ["mail"]="farshadnassiri@gmail.com"
quotes = [
    "The best way to predict the future is to invent it. – Alan Kay",
    "A dream doesn't become reality through magic; it takes sweat, determination, and hard work. – Colin Powell",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. – Albert Schweitzer",
    
]
def send_email(recipient_name, recipient_email):
    subject="Your Daily Inspirational Quote"
    quote=random.choice(quotes)
    body = f"Hello {recipient_name}, here is your daily inspirational quote:\n\n{quote}"
    message=MIMEMultipart()
    message["from"]=os.environ.get("mail")
    message["to"]=recipient_email
    message["subject"]=subject
    message.attach(MIMEText(body,"plain"))

    try:
        session=smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(os.environ.get("mail"),os.environ.get("mailpassword"))
        text = message.as_string()
        session.sendmail(os.environ.get("mail"), recipient_email, text)
        session.quit()
        print(f"Mail Sent Successfully to {recipient_name} ({recipient_email})")

    except Exception as e:
         print(f"Failed to send email to {recipient_name} ({recipient_email}). Error: {e}")

if __name__ == "__main__":

        mymail=send_email("farshad","farshadnassiri@gmail.com")