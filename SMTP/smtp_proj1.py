# -*- coding:UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方 SMTP 服务
mail_host = 'smtp.163.com'
mail_port = 25
mail_username = 'sgipservice@163.com'
mail_pwd = 'sgipservice123'

sender = 'sgipservice@163.com'
receivers = ['2890638099@qq.com']

mail_msg = '''
<p>Python mail send...</p>
<p><a href="http://www.baidu.com">This is a link.</a></p>
'''

# 三个参数依次表示：文件内容，设置文本格式，设置编码
# message = MIMEText('Python 邮件发送...', 'plain', 'utf-8')
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header('菜鸟教程', 'utf-8')
message['To'] = Header('Hello', 'utf-8')

subject = 'Python SMTP 邮件'
message['Subject'] = Header(subject, 'utf-8')



try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, mail_port)
    smtpObj.login(mail_username, mail_pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('Send Success!')
except smtplib.SMTPException as error:
    print('Error,Send mail fail!')
    print(error)

'''
发送不成功，错误提示：
554 DT:SPM 发送的邮件内容包含了未被许可的信息，
或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；
'''