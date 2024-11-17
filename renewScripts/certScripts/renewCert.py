class renewCert:
    
    def __init__(self, ip, application, domain):
        self.ip = ip
        self.application = application
        self.domain = domain
    
    def getIp(self):
        return self.ip
    
    def getApplication(self):
        return self.application
    
    def getDomain(self):
        return self.domain
    
    def renew(self):
        pass
    