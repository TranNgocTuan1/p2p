import logging

class Ping():

    """
    method for pingin serevr client is connected to
    :param client: client to send response to
    :param data: parameter for code unification
    """
    def ping(self, client, data, log):
        try:
            print(client.ip)
            client.conn.send(bytes('TRANSLATEPONG\"Tuanuv slovnik\"\r\n', "utf-8"))
            logging.info(str(client.ip)+"=client ping success")
        except:
            client.conn.send(bytes('TRANSLATEDERR\"neco se pokazilo\"\r\n', "utf-8"))
            logging.error(str(client.ip)+"=client ping unsuccessful")