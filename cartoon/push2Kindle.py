import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders


_user = "522132087@qq.com"
_pwd = "rolev@6541"
_to = "deyangchu@gmail.com"

def send_email():
    path = '/home/deyangchu/manga'
    files = os.listdir(path)
    for file in files:
        if os.path.splitext(file)[1] == ".pdf":
            file_path = os.path.join(path,file)
            msg = MIMEMultipart()
            msg['Subject'] = 'convert'
            msg['From'] = _user
            msg['To'] = _to
            attfile = file_path
            basename = os.path.basename(file_path)
            print(basename)
            fp = open(attfile,'rb')
            att = MIMEText(fp.read(),'base64','gbk')
            att['Content_Type'] = 'application/octer-stream'
            att.add_header('Content-Disposition','attachment',filename=('gbk','',basename))
            encoders.encode_base64(att)
            msg.attach(att)
            s = smtplib.SMTP_SSL("smtp.qq.com",465,timeout = 30)
            s.login(_user,_pwd)
            s.sendmail(_user,_to, msg.as_string())
            s.close

send_email()
# os.system('rm -rf %s/*'%settings.IMAGES_STORE)