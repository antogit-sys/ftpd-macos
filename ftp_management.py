from os import system, path
from subprocess import run

class ftpMan:
	def __init__(self):
		self.path='/System/Library/LaunchDaemons/ftp.plist'
		self.isFile = path.isfile(self.path)
		self.status = None
	
	def setPath(self, newPath):
		self.path = newPath
	
	def getPath(self):
		return self.path
	
	def getStatus(self):
		return self.status
	
	def download_plist(self):	
		system("""
			wget https://opensource.apple.com/source/lukemftpd/lukemftpd-47/ftp.plist &&
			sudo mv ftp.plist '/System/Library/LaunchDaemons/ftp.plist'
		""")
	



