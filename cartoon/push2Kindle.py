import os.path, json
import smtplib, requests, time
from wechat_sender import Sender
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from settings import IMAGES_STORE as mangapath
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def jpg2mobi():
    os.chdir(mangapath)
    folders = [name for name in os.listdir(mangapath) if os.path.isdir(name)]
    #print(os.getcwd())
    for folder in folders:
        os.system('kcc-c2e -p KV -u -r 1 %s/' % folder) # -u: upscale photo size, -r 1: combine double page and rotate
def send2wechat(title):
    sender = Sender(receivers='漫画更新push！',token='rolevblf')
    sender.send('Comic updated! Download on Kindle from secret url!%s'%title)

def pushmessage(title):
    requests.post(
        'https://api.alertover.com/v1/alert',
        data={
            'source':'s-6ff6f42b-68c4-4daa-b1eb-b7444d18',
            'receiver':'u-3c76edda-e339-48d6-82e9-95d1a4b0',
            'title':'New Comic Update!',
            'content':'Comic updated! Download on Kindle from secret url!%s'%title
        }
    )

_user = "jiaruchy@gmail.com"
_pwd = "wangming"
_to = "chudeyang@kindle.cn"

def list_file():
    path = mangapath
    files = os.listdir(path)
    newfiles = []
    for i in files:
        if os.path.splitext(i)[1] == ".mobi" and (time.time()-os.path.getctime('%s/%s'%(path,i))<7200):
            newfiles.append(os.path.splitext(i)[0])
    return newfiles

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
            #print(basename)
            fp = open(attfile,'rb')
            att = MIMEText(fp.read(),'base64','gbk')
            att['Content_Type'] = 'application/octer-stream'
            att.add_header('Content-Disposition','attachment',filename=('gbk','',basename))
            encoders.encode_base64(att)
            msg.attach(att)
            s = smtplib.SMTP_SSL("smtp.gmail.com",465,timeout = 300)
            s.login(_user,_pwd)
            s.sendmail(_user,_to, msg.as_string())
            s.close
            newfiles.append(os.path.splitext(file)[0])
            time.sleep(10)
    return newfiles

jpg2mobi()
os.system('find %s -mindepth 1 -maxdepth 1 -type d -exec rm -r {} \;'%mangapath) # Delete all folders in directory(raw JPEG files)
#newfiles = send_email()
newfiles = list_file()
try:
    with open (BASE_DIR+'/cartoon/logg.txt','r') as r, open (BASE_DIR+'/cartoon/data.json','r') as raw:
        data = json.load(raw)
        data['filenum'] = r.readlines()[0]
        data['eptitle'] = newfiles[-1]

    with open(BASE_DIR+'/cartoon/data.json','w') as w:
        json.dump(data, w, indent = 4, ensure_ascii=False)
except IndexError:
    pass
except Exception as e:
    print(e)

string=''
for file in newfiles:
    string = string+'\n'+file
if string!='':
    pushmessage(string)
    send2wechat(string)
# os.system('rm -rf %s/*'%settings.IMAGES_STORE)
