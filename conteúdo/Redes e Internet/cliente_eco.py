#!/usr/bin/env python
# cliente_eco.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) 
    for i in range(3):
        s.sendall(b"Oi, Tudo Bem?")
        data = s.recv(1024)
        print(f"{i}: Received {data!r}")
    s.sendall(b"Fim")
    print (f"{s.recv(1024)}")
