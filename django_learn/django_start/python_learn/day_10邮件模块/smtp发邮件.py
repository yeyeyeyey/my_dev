from email.mime.text import MIMEText
msg = MIMEText('hello ,it is sended by python','plain','utf-8')
#第一个参数是发送内容，第二个表示纯文本，第三个是编码格式

from_addr = input('from:  ')
password = input('password')

to_addr = input("wanna send to :")

smtp_server = input('SMTP server: ')
import smtplib
server = smtplib.SMTP(smtp_server,25)#smtp协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()