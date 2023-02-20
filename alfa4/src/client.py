class Client:
    """
    a constructor for a client for easier access (client coneected through putty/telnet)
    """
    def __init__(self, conn, ip):
        self.conn = conn
        self.ip = ip