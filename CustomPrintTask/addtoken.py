# Author : Pri0ri7y
# Github : https://github.com/pri0ri7y
# Adds token to the given secured service.

import arcpy
import httplib
import urllib
import json


class TokenHandler:

	def __init__(self):
	
	    # Server Configuration  Ex: http://system.domain.com/webadapter/rest/services
		self.tokenURL = "/webadapter/admin/generateToken"
		self.userName = "username"
		self.password = "password"
		self.serverName = "system"
		self.server = "system.domain.com"
		
		# initiating process
		self.main()
		
	def main(self):
	
		self.inputJSON = arcpy.GetParameterAsText(0)		 
		self.jsonObj = json.loads(self.inputJSON)
		self.token = self.getToken()		 
		self.TokenJSON = self.addTokenToJSON(self.jsonObj,self.token)
		self.correctedJSON = str(json.JSONEncoder().encode(self.TokenJSON))
		arcpy.SetParameterAsText(1,self.correctedJSON)
		 
		
	def getToken(self):
		# Token URL is typically http://server[:port]/arcgis/admin/generateToken		
		# URL-encode the token parameters:-
		self.params = urllib.urlencode({'username': self.userName, 'password': self.password, 'client': 'requestip', 'f': 'json'})		
		self.headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}		
		# Connect to URL and post parameters
		httpConn = httplib.HTTPConnection('system.domain.com')
		httpConn.request("POST", self.tokenURL, self.params, self.headers)		
		# Read response
		response = httpConn.getresponse()
		if (response.status != 200):
			httpConn.close()
			print "Error while fetch tokens from admin URL. Please check the URL and try again."
			return
		else:
			data = response.read()
			httpConn.close()           
			# Extract the token from it
			token = json.loads(data)        
			return token['token']
			
			
	def addTokenToJSON(self,JSON,Token):
		for operationalLayers in JSON['operationalLayers']:
			if 'url' in operationalLayers:
				 if operationalLayers['url'].find(self.serverName) > 1:
					 operationalLayers['Token'] = Token

		return JSON



if __name__ == "__main__":

    tokenHandler = TokenHandler()
