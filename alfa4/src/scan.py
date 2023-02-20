import socket
import ipaddress
import os
import logging


class Scan:
    """
    constructor for the Scan class which acts as a TRANSLATESCAN command
    """

    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(script_dir, '../config/ipAporty.txt'), 'r') as f:
            lines = f.readlines()
        ips = lines[0].split("-")
        ports = lines[1].split("-")
        self.firstIP = ipaddress.ip_address(ips[0].strip())
        self.lastIP = ipaddress.ip_address(ips[1].strip())
        self.firstPort = int(ports[0].strip())
        self.lastPort = int(ports[1].strip())

    """
    method for scanning the network using the file ipAporty.txt in config directory
    :param client: client to send response to
    :param word: word to translate
    """

    def scan_net(self, client, word, log):
        ipsa = []
        cur = self.firstIP
        port = self.firstPort
        translate = False
        while True:
            if cur == self.lastIP+1:
                break
            while True:
                if port == self.lastPort+1:
                    cur += 1
                    port = self.firstPort
                    break
                ipsa.append((cur, port))
                port += 1
        for i in ipsa:
            try:

                client_socket = socket.socket()
                client_socket.settimeout(0.1)
                client_socket.connect((str(i[0]), i[1]))
                client_socket.send(bytes('TRANSLATELOCL\"' +word+'\"', "utf-8"))
                data = client_socket.recv(1024).decode()
                mylist = data.split('\"')
                if mylist[0] == 'TRANSLATEDSUC':
                    logging.info(str(client.ip) + f'=translate word from {str(i[0])}:{i[1]} successfully')
                    client.conn.send(bytes(data + '\r\n', "utf-8"))
                    translate = True
                    break
                if str(i[0]) != "127.0.0.1" and str(i[0]) != client.conn.getsockname()[0]:
                    client_socket.close()
            except:
                pass
        if not translate:
            client.conn.send(bytes('TRANSLATEDERR"slovo neslo prelozit"\r\n', "utf-8"))
            logging.error(str(client.ip) + f"=translate word from scan not successfull")

