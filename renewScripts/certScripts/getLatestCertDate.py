
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
         
         return date format yyyy-mm-ddThh:mm:ss, if cause exception print error massage and exit with code 1
        
        """
        self.apiUrl= 'http://' + self.getIp() + '/certs/latest'
        self.params = {"application":self.getApplication(), "domain": self.getDomain()}
        
        try:
            self.res = requests.get(self.apiUrl, params=self.params)
            if (self.res.status_code == 200):
                # Truncate msec
                return 0, self.res.json()["date"].split(".")[0]
            else:
                return 1, "Cannot get data, status code: " + self.res.status_code
        except requests.exceptions.RequestException as e:
            return 1, e