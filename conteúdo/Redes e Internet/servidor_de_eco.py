#!/usr/bin/env python
# servidor_de_eco.py

import socket

HOST = "127.0.0.1"  # endereço IP da máquina local
PORT = 65432  # Porta em que vamos escutar (portas não privilegiadas > 1023).

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # cria o Socket
    s.bind((HOST, PORT)) # Conecta o socket ao host e porta
    s.listen() # começa a escutar...
    conn, addr = s.accept() # Aceita a conexão
    with conn:
        print(f"Connectado por {addr}")
        while True:
            data = conn.recv(1024) # Tenta receber dados
            if not data:
                break
            conn.sendall(data) # Envia de volta os dados (eco)