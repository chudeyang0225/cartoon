import os.path, json
import smtplib, requests, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mangapath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/cartoon/manga'
print(mangapath)

def jpg2mobi():
    folders = os.listdir(mangapath)
    os.chdir(mangapath)
    print(os.getcwd())
    for folder in folders:
        print(folder)
        os.system('kcc-c2e -p KV -u -r 1 %s/' % folder) # -u: upscale photo size, -r 1: combine double page and rotate


def pushmessage(title):
    requests.post(
        'https://api.alertover.com/v1/alert',
        data={
            'source':'s-6ff6f42b-68c4-4daa-b1eb-b7444d18',
            'receiver':'u-3c76edda-e339-48d6-82e9-95d1a4b0',
            'title':'New Comic Update!',
            'content':'Comic updated! Check Kindle!%s'%title
        }
    )

_user = "522132087@qq.com"
_pwd = "rolev@6541"
_to = "chudeyang@kindle.cn"

def send_email():
    path = mangapath
    files = os.listdir(path)
    newfiles = []
    for file in files:
        if os.path.splitext(file)[1] == ".mobi":
            file_path = os.path.join(path,file)
            msg = MIMEMultipart()
            msg['Subject'] = ''
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
            s = smtplib.SMTP_SSL("smtp.qq.com",465,timeout = 300)
            s.login(_user,_pwd)
            s.sendmail(_user,_to, msg.as_string())
            s.close
            newfiles.append(os.path.splitext(file)[0])
            time.sleep(10)
    return newfiles

jpg2mobi()
newfiles = send_email()

with open (BASE_DIR+'/cartoon/logg.txt','r') as r, open (BASE_DIR+'/cartoon/data.json','r') as raw:
    data = json.load(raw)
    data['filenum'] = r.readlines()[0]
    data['eptitle'] = newfiles[-1]

with open(BASE_DIR+'/cartoon/data.json','w') as w:
    json.dump(data, w, indent = 4)


string=''
for file in newfiles:
    string = string+'\n'+file
if string!='':
    pushmessage(string)
# os.system('rm -rf %s/*'%settings.IMAGES_STORE)