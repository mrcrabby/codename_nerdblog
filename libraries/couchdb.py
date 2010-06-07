'''
Created on Jun 6, 2010

@author: dro
'''
import httplib, json, re

class Root():
    def __init__(self):
        self.couch = httplib.HTTPConnection("localhost:5984")
    
    def _json_response(self):
        return json.loads(self.couch.getresponse().read().strip())
    
    
class DB(Root):
    def get_all(self):
        self.couch.request("GET", "/_all_dbs")
        return self._json_response()
    
    def get_info(self,dbname):
        dbname = re.sub(r'[\s]','_',dbname.lower())
        self.couch.request("PUT", "/%s/" % dbname)
        return self._json_response()
        
    def create(self,dbname):
        dbname = re.sub(r'[\s]','_',dbname.lower())
        self.couch.request("PUT", "/%s/" % dbname)
        response = self.couch.getresponse()
        if response.status == '201':
            return True
        else:
            return False
        
    def delete(self,dbname):
        dbname = re.sub(r'[\s]','_',dbname.lower())
        self.couch.request("DELETE", "/%s/" % dbname)
        response = self.couch.getresponse()
        if response.status == '200':
            return True
        else:
            return False
    
            