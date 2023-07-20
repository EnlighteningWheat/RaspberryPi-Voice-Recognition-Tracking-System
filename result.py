import socket
import os
import sys
import struct


def send_txt():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 192.168.199.1和8088分别为服务端（pc）的IP地址和网络端口
        s.connect(('192.168.50.1', 8003))
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))

    while True:
        # filepath是要被发送图片的路径
        filepath = r'D:\AI_project\gluoncv\result.txt'
        fhead = struct.pack(b'128sl', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)
        s.send(fhead)
        print('client filepath: {0}'.format(filepath))

        fp = open(filepath, 'rb')
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} 发送成功...'.format(filepath))
                break
            s.send(data)
        s.close()
        break



