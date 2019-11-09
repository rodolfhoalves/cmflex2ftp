
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
    mail_content = '''Arquivos enviados para o BI com sucesso - ITECNOVE'''

    #The mail addresses and password
    sender_address = 'directionsystems@gmail.com'
    sender_pass = 'JgT9!H!C0NhNw@3yG2f3#*8vYrIGiAQl4rJgdb%9f0qKWVON&j3#gqedMejw#3QXQEH$vy5%#lDwFI@NBg$fp0U@*O2RgRZ%T!r!'
    receiver_address = 'rodolfho.queiroz@ponteshoteis.com.br'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Arquivos enviados para o BI - ITECNOVE'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
