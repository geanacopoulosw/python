import socket


class LanScanner:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.networkIP = socket.gethostbyname(self.hostname)
        self.networkPrefix = self.networkIP.split(".")
        del(self.networkPrefix[-1])
        self.networkPrefix = ".".join(self.networkPrefix)

    def check(self, current):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.01)
        if not s.connect_ex((current, 135)):
            s.close()
            return 1
        else:
            s.close()

    def start(self):
        print('Your IP: %s' % self.networkIP)
        print('Scanning LAN network....')
        for ip in range(1, 255):
            current = self.networkPrefix + '.' + str(ip)
            if self.check(current):
                print('%s \t- %s' % (current, socket.getfqdn(current)))
        print("scan finished")


if __name__ == '__main__':
    sLan = LanScanner()
    sLan.start()






