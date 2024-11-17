import json
import requests


class getLatestCertDate():
    
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
         
    def getLatestCertDate(self):
        """
         get latest certifcation update date
         
         return date format yyyy/mm/ddThh:mm:ss, if cause exception print error massage and exit with code 1
        
        """
        self.apiUrl= 'http://' + self.getIP() + '/certs/latest'
        self.params = {"application": + self.getApplication(), "domain": self.getDomain()}
        
        try:

            self.res = requests.get(self.apiUrl, params=self.params)
            if (self.res.status_code in [200, 201]):
                return self.res.json()
        except requests.exceptions.RequestException as e:
            return e