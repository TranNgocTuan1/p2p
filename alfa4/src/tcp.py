import socket
import logging
from threading import Thread
from client import Client
from local import Local
from scan import Scan
from ping import Ping

import os


class Tcp:
    """
    constructor for Tcp class (setting up server)
    """
    def __init__(self):
        self.local = Local()
        self.ping = Ping()
        self.scan = Scan()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(script_dir, '../log/log.log')
        logging.basicConfig(filename=self.filename, level=logging.INFO)
        self.commands = {
            "TRANSLATELOCL" : self.local.translate_local,
            "TRANSLATESCAN" : self.scan.scan_net,
            "TRANSLATEPING" : self.ping.ping
        }
        server_inet_address = ("192.168.43.152", 65435)
        self._isRunning = True
        self.server_socket = socket.socket()
        self.server_socket.bind(server_inet_address)
        self.server_socket.listen()

        self.Method()

    """
    a method for multiple client connections
    """
    def Method(self):
        while self._isRunning:
            try:
                connection, client_inet_address = self.server_socket.accept()
                client = Client(connection, client_inet_address)
                x = Thread(
                    target=Tcp.LoopClients, args=(self, client,))
                logging.info(str(client.ip)+'=client connected')
                x.start()

            except Exception as e:
                pass
    """
    A method for client service
    :param client: client
    """
    def LoopClients(self, client):
        while True:
            try:
                data = client.conn.recv(1024).decode() 
                if data.startswith("TRANSLATE"):
                    mess = data.split('\"')
                    self.commands[mess[0]](client, mess[1], self.filename)
                elif data.startswith("exit") or data.startswith("EXIT"):
                    logging.info(str(client.ip)+'=client disconnected')
                    break
            except Exception as e:
                client.conn.send(bytes('TRANSLATEDERR\"neco se pokazilo\"\r\n', "utf-8"))
        client.conn.close()
