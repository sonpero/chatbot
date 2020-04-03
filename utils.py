import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

# message = "turlututu chapeau pointu"
# person_name = "Alex"
# email = "toto.tata@truc.com"

def mail(message, person_name, email):

    # load yml file to dictionary
    credentials = yaml.load(open('./credentials.yml'))

    # access values from dictionary
    username = credentials['gmail']['username']
    password = credentials['gmail']['password']

    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    msg['From'] = email
    msg['To'] = username
    msg['Subject'] = "Rasa BOT Message de " + person_name + " " + email

    # attach image to message body
    # msg.attach(MIMEImage(open("fichier.jpg", "rb").read()))

    # text du message
    body = message
    msg.attach(MIMEText(body, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    # Login Credentials for sending the mail
    server.login(username, password)

    # send the message via the server.
    try:
        server.sendmail(email, msg['To'], msg.as_string())
        print("message envoyé")
        succes = True
    except:
        print("echec envoi mail")
        succes = False

    server.quit()
    return succes

#mail(message, person_name, email)