# -*- coding:GBK -*-
import configparser
import smtplib
#发送附件
from testdata.getpath import GetTestConfig
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import mimetypes
import os

class MyMail:
    def __init__(self,mail_config_file):
        config=configparser.ConfigParser()
        config.read(mail_config_file)

        self.smtp=smtplib.SMTP_SSL()
        self.login_user=config.get('SMTP','login_user')
        self.login_pwd=config.get('SMTP','login_pwd')
        self.from_addr=config.get('SMTP','from_addr')
        self.to_addr=config.get('SMTP','to_addr')
        self.host=config.get('SMTP','host')
        # self._host=smtp.qq.com
        self.port=config.get('SMTP','port')
        # print(self.host)

    # 连接到服务器
    def connect(self):
        # self.smtp.set_debuglevel(True)
        # self.smtp.starttls()
        # print(self.host)
        # print(self.port)
        self.smtp.connect(self.host, self.port)
        # self.smtp.connect(self._host)
        # self.smpt=smtplib.SMTP_SSL(self._host,self.port)
        print("成功")

    # 登陆邮件服务器
    def login(self):
        try:
            self.smtp.login(self.login_user, self.login_pwd)
            print('成功')
        except Exception as e:
            print("失败")
            print('%s' % e)

    # 发送邮件
    def send_mail(self, mail_subject, mail_content, attachment_path_set):
        # 构造MIMEMultipart对象做为根容器
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        # msg['To'] = self.to_addr
        msg['To'] = ','.join(eval(self.to_addr))
        # 注意，这里的msg['To']只能为逗号分隔的字符串，形如 'sdxx@163.com', 'xdflda@126.com'
        msg['Subject'] = mail_subject
        # 添加邮件内容
        content = MIMEText(mail_content, "html", _charset='gbk')
        #说明，这里_charset必须为gbk和# -*-coding:GBK-*- 保持一致，否则邮件内容乱码

        msg.attach(content)

        for attachment_path in attachment_path_set:
            if os.path.isfile(attachment_path):#如果附件存在
                type,coding=mimetypes.guess_type(attachment_path)
                if type==None:
                    type='application/octet-stream'

                major_type,minor_type=type.split('/',1)
                with open(attachment_path,'rb') as file:
                    if major_type=='text':
                        attachment=MIMEText(
                            file.read(),_subtype=minor_type,_charset='GB2312')
                    elif major_type=='image':
                        attachment=MIMEImage(
                            file.read(),_subtype=minor_type)
                    elif major_type=='application':
                        attachment=MIMEApplication(
                            file.read(),_subtype=minor_type)
                    elif major_type=='audio':
                        attachment=MIMEAudio(
                            file.read(),_subtype=minor_type)

                #修改附件名称
                attachment_name=os.path.basename(attachment_path)
                attachment.add_header(
                    'Content-Disposition','attachment',filename=('gbk','',attachment_name))
                #说明，这里的('gbk','',attachment_name)解决了附件为中文名称时，显示不对的问题

                msg.attach(attachment)

        #得到格式化后的完整文本
        full_text=msg.as_string()

        #发送邮件
        self.smtp.sendmail(self.from_addr,eval(self.to_addr),full_text)

    #退出
    def quit(self):
        self.smtp.quit()

# print(GetTestConfig('mail.conf'))
# mymail=MyMail(GetTestConfig('mail.conf'))
# mymail.connect()
# mymail.login()
# mail_content='附件为测试报告，请查收'
# mail_title='【测试报告】接口测试报告'
#
# attachments=set(
#     ['F:\\python\\apiauto\\day6\\testreport\\2018-10-24-19-58-00-TestReport.xlsx']
# )
#
# mymail.send_mail(mail_title,mail_content,attachments)
# mymail.quit()