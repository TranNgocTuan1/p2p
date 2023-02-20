import os
import logging

class Local:
    """
    constuctor for class Local which acts as a TRANSLATELOCL command
    """
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(script_dir, '../config/slovnik.txt'), 'r') as f:
            lines = f.readlines()
        self.dictionary = {}
        for line in lines:
            word = line.split(":")
            self.dictionary[word[0].strip()] = word[1].strip()

    """
    method that is trying to translate a word on this server
    :param client: client to send response to
    :param word: word to translate
    """
    def translate_local(self, client, word, log):
        try:
            mess = bytes('TRANSLATEDSUC\"'+ self.dictionary[word] +'\"\r\n', "utf-8")
            client.conn.send(mess)
            logging.info(str(client.ip)+"=clients word translated")
        except:
            mess = bytes('TRANSLATEDERR\"slovo neni v localnim slovniku\"\r\n', "utf-8")
            client.conn.send(mess)
            logging.error(str(client.ip)+"=clients word not translated")




