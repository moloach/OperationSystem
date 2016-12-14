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
    用socket发送http请求判断服务的健壮度
    """
  
    def __call__(self,address, port):
        self.address = address
        self.port = port
        #self.resource = resource
        return Check

    def check(self,address,port):
        #if not self.resource.startswitch('/'):
            #self.resource = '/' + self.resource

        request = 'GET / HTTP/1.1\r\nHOST:%s\r\n\r\n' %address

        s = socket.socket()

        s.settimeout(10)

        #print("start to connect %s on the  %s port......." %(self.address,int(self.port)))

        try:
            s.connect((address,port))
            print("cocnnect %s on port %s success!" %(address,port))
            s.send(request)
            response = s.recv(100)

        except socket.error as e:
            #print("connect host %s on port %s fail??reason is %s" %(self.address,self.port,e))
            return 'connect error'

        finally:
            s.close()

        line = StringIO(response).readline()

        try:
            (http_version, status, messages) = re.split(r'\s+',line,2)

        except ValueError:
            #print("?ָ???Ӧ??ʧ??")
            return 'error'
        #print ("return status Code is %s" %(status))

        if status in ['200', '301', '302']:
            #print('server status is well')
            return status
        else:
            #print('????????????״̬')
            return status

checks = Check()
data = database.Database()

def get_update_host():
    server_data = data.get_host()
    server_loop = []
    for item in server_data:
            a = {
                'check_IP':item['IP_address'],
                'port':item['port'],
                'cycle':item['cycle']
                }
            server_loop.append(a)
    return server_loop


def save_server_status():
    while True:
        check_result = []
        server_loop = get_update_host()
        #
        for item in server_loop:
            check_IP = item['check_IP']
            #print(check_IP)
            check_port = item['port']       
            check_result.append(checks.check(check_IP,check_port))
            time.sleep(item['cycle'])
        data.save_check_status(check_result)
        


if __name__ == "__main__":
    save_server_status()
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
parser.add_option('-a','--address',dest = "address", default = 'localhost',help='Ҫ????????????ַ')
parser.add_option('-p','--port',dest = 'port',default = 80, help = "Ҫ???????????˿?")
parser.add_option('-r','--resource',dest = 'resource', default = '/', help = 'Ҫ????????Դ')
(options, args) = parser.parse_args()


checks = Check(options.address,options.port,options.resource)
while True:
    checks.check()
    print("=======================")
    time.sleep(10)


?????????У?ִ?нű? python check_server.py --address hostname --resource ·?? --port ?˿?????
notice?? ·??Ҫ????'/ ' ǰ׺
example??python check_server.py  --address 121.199.62.174 --resource /js/tmpl/login.ejs?.. --port 15672

'''
