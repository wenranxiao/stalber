from email.mime.text import MIMEText
import smtplib

from oslo_log import log as logging
from oslo_config import cfg


mail_opts = [
    cfg.StrOpt('mail_server',
               default='smtp.qq.com',
               help='mail server'),
    cfg.IntOpt('mail_port',
               default='465',
               help='mail port'),
    cfg.StrOpt('subject',
               default='stalber test',
               help='mail subject'),
    cfg.StrOpt('mail_username',
               default='1285453723@qq.com',
               secret=True,
               help='mail user name'),
    cfg.StrOpt('mail_password',
               default='dnqqrzkkjuribahd',
               secret=True,
               help='mail password'),
    cfg.ListOpt('receivers',
                default='wenranxiao@gmail.com',
                help='email addresses'),
]


CONF = cfg.CONF
CONF.register_opts(mail_opts, 'email')
CONF.register_opts(mail_opts)
LOG = logging.getLogger(__name__)

def send_mail(receivers, subject=None, body=None):

    body = 'This stalber test.'
    msg = MIMEText(body, 'plain', 'utf-8')
    mail_user = CONF.email.mail_username
    mail_pass = CONF.email.mail_password
    msg['From'] = mail_user
    msg["To"] = ','.join(CONF.email.receivers)
    msg["Subject"] = CONF.email.subject
    receivers = CONF.email.receivers
    server = smtplib.SMTP_SSL(CONF.email.mail_server, CONF.email.mail_port)
    #server = smtplib.SMTP(CONF.email.mail_server, 25)
    server.set_debuglevel(1)
    server.login(mail_user, mail_pass)
    server.sendmail(mail_user, receivers, msg.as_string())
    server.quit()

if __name__ == "__main__":
    result = send_mail(CONF.receivers)
    print result
