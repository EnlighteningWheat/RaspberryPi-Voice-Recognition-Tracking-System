import socket
import os
import sys
import struct

import result
import scanimage


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # IP地址留空默认是本机IP地址
        s.bind(('192.168.50.107', 8086))
        s.listen(7)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print("连接开启，等待传图...")

    sock, addr = s.accept()
    deal_data(sock, addr)
    s.close()


def deal_data(sock, addr):
    print("成功连接上 {0}".format(addr))

    while True:
        fileinfo_size = struct.calcsize('128sl')
        buf = sock.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sl', buf)
            fn = filename.decode().strip('\x00')
            # PC端图片保存路径
            new_filename = os.path.join('D:\AI_project\gluoncv', fn)

            recvd_size = 0
            fp = open(new_filename, 'wb')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = sock.recv(1024)
                    recvd_size += len(data)
                else:
                    data = sock.recv(1024)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
        sock.close()
        try:
            class_id, scores, bounding_boxs = scanimage.scan(r'D:\AI_project\gluoncv\image.png')
            # # print('class_id:', class_id)
            # # print('scores:', scores)
            # # print('bounding_boxs:', bounding_boxs)
            os.remove(r'D:\AI_project\gluoncv\image.png')
            file = open(r"D:\AI_project\gluoncv\result.txt", 'w')
            file.write(str(class_id))
            file.write('\n')
            file.write(str(scores))
            file.write('\n')
            file.write(str(bounding_boxs))
        except:
            print("图片不完整")
            os.remove(r'D:\AI_project\gluoncv\image.png')
            file = open(r"D:\AI_project\gluoncv\result.txt", 'w')
            file.write("\n[-2.]\n<NDArray 1 @cpu(0)>\n")
            file.write('\n[-2.]\n<NDArray 1 @cpu(0)>\n')
            file.write("\n[-2 -2 -2 -2]\n<NDArray 4 @cpu(0)>")

        break


if __name__ == '__main__':
    socket_service()