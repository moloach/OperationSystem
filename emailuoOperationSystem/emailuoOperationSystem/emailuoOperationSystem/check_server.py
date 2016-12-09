#!/usr/bin/env python
#coding= utf-8

#from optparse import OptionParser
import socket
import time
import sys
import re
from StringIO import StringIO
import pymongo
import database


class Check(object):
    """
    用socket建立一个连接，发送http请求，根据返回的状态码来判断服务的健壮度
    """
  
    def __call__(self,address, port):
        self.address = address
        self.port = port
        #self.resource = resource
        return Check

    def check(self,address,port):
        #if not self.resource.startswitch('/'):
            #self.resource = '/' + self.resource

        request = 'GET / HTTP/1.1\r\nHOST:%s\r\n\r\n' %( address)

        s = socket.socket()

        s.settimeout(10)

        #print("start to connect %s on the  %s port......." %(self.address,int(self.port)))

        try:
            s.connect((address,port))
            print("cocnnect %s on port %s success!" %(address,port))
            s.send(request)
            response = s.recv(100)

        except socket.error,e:
            #print("connect host %s on port %s fail，reason is %s" %(self.address,self.port,e))
            return 'error3'

        finally:
            s.close()

        line = StringIO(response).readline()

        try:
            (http_version, status, messages) = re.split(r'\s+',line,2)

        except ValueError:
            #print("分隔响应码失败")
            return 'error1'
        #print ("return status Code is %s" %(status))

        if status in ['200', '301', '302']:
            #print('server status is well')
            return status
        else:
            #print('请检查服务器状态')
            return 'error2'

checks = Check()
data = database.Database()
server_data = data.get_host()

server_loop = []
for item in server_data:
        a = {
            'check_IP':item['IP_address'],
            'port':item['port']
            }
        server_loop.append(a)


def get_server_status():
    for item in server_loop:
        check_IP = item['check_IP']
        #print(check_IP)
        check_port = item['port']       
        check_result = checks.check(check_IP,check_port)
        return check_result
#time.sleep(5)
'''
#the function have loop-function
def check_server():
    while True:
        status = []
        try:
            for item in server_data:
                check_ip = item['IP_address']
                check_port = item['port']
                check_result = checks.check(check_ip,check_port)
                status.append({'server_name':check_result})
            return status
        except:
            return 'Noack'

def get_server_status():
'''
'''
parser = OptionParser()
parser.add_option('-a','--address',dest = "address", default = 'localhost',help='要检查的主机地址')
parser.add_option('-p','--port',dest = 'port',default = 80, help = "要检查的主机端口")
parser.add_option('-r','--resource',dest = 'resource', default = '/', help = '要检查的资源')
(options, args) = parser.parse_args()


checks = Check(options.address,options.port,options.resource)
while True:
    checks.check()
    print("=======================")
    time.sleep(10)


在命令行中，执行脚本 python check_server.py --address hostname --resource 路径 --port 端口数据
notice： 路径要加上'/ ' 前缀
example：python check_server.py  --address 121.199.62.174 --resource /js/tmpl/login.ejs?.. --port 15672

'''
