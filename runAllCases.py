import HTMLTestRunner
import unittest
import time
import os
import sys
import requests
import yaml
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from ruamel import yaml

base_path = os.path.dirname(os.path.relpath(__file__))


def login():
    # 登录获取token
    url = "https://api.ezbtest.top/uc/login"
    data = {"username": '1656481004@qq.com', "password": 'zxz123abc'}
    res = requests.post(url=url, data=data)
    dc = res.json()
    token = dc['data']['token']
    return token


def write_yaml(value):
    # yamlPath yaml文件路径
    yamlPath = os.path.join(base_path, 'common', 'token.yaml')
    # 需要写入的内容
    tk = {'token': value}
    # 写入到yaml文件
    with open(yamlPath, 'w', encoding='utf-8') as f:
        yaml.dump(tk, f, Dumper=yaml.RoundTripDumper)


# 查找最新生成的测试报告html
def new_file(test_dir):
    # 列举test_dir目录下所有的文件，结果以列表的形式返回
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    file_path = os.path.join(test_dir, lists[-1])
    # print(file_path)
    return file_path


# 发送最新的html测试报告
def send_email(newfile):
    f = open(newfile, 'rb')
    mail_body = f.read()
    f.close()
    # 发送邮箱
    sender = 'qunjie_xu@proway.tech'
    # 多个接受邮箱,单个收件人的话，直接是receiver=’xxx@163.com'
    receiver = ['qunjie_xu@proway.tech','1991789649@qq.com']
    # 发送邮件主题
    subject = '自动化测试报告'
    # 发送附件
    msg = MIMEMultipart('mixed')
    # 邮件正文是MIMEText
    msg_html = MIMEText(mail_body, 'html', 'utf-8')  # 邮件正文显示的内容
    msg.attach(msg_html)
    msg['From'] = 'qunjie_xu@proway.tech'
    msg['To'] = ";".join(receiver)
    # msg['To'] = 'qunjie.xu@chyeth.com'
    msg['Subject'] = Header(subject, 'utf-8')
    # 连接发送邮件
    smtpserver="smtp.mxhichina.com"
    smtp = smtplib.SMTP_SSL(smtpserver)
    smtp.connect(smtpserver, 465)
    user='qunjie_xu@proway.tech'
    password='zxz!123!abc!'
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + r'\..')  # 返回脚本的路径
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./log/logs.txt',
                    filemode='w')
if __name__ == "__main__":
    token = login()  # 登录获取token
    write_yaml(token)  # 写入yaml文件
    test_dir = 'D:\\puwei\\InterfaceTest\\testCases\\'
    test_report = 'D:\\puwei\\InterfaceTest\\testReports\\'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    fileName = test_report + now + 'result.html'
    fp = open(fileName, 'wb')
    runner = HTMLTestRunner.HTMLTestReportCN(stream=fp, title='自动化测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()
    new_report = new_file(test_report)
    send_email(new_report)
