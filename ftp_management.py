from os import path
from subprocess import run
from wget import download
from shutil import move

class ftpMan:
	def __init__(self):
		self.path='/System/Library/LaunchDaemons/ftp.plist'
		self.isFile = path.isfile(self.path)
		self.status = None
		self.path_home = path.expanduser("~")
		self.path_profile = self.path_home+str("/.profile")
		self.path_bashrc = self.path_home+str("/.bashrc")  
	
	def setPath(self, newPath):
		self.path = newPath
	
	def getPath(elf):
		return self.path
	
	def getStatus(self):
		return self.status
	
	def download_plist(self):	
		download("https://opensource.apple.com/source/lukemftpd/lukemftpd-47/ftp.plist", "ftp.plist")
		move("ftp.plist", self.path)
	
	def ftp_status(self):
		cmd = run(['sudo', 'launchctl', 'list'], shell=False, capture_output=True)
		output = cmd.stdout.decode()
		if "com.apple.ftpd" in output:
			self.status = "on"
		else:
			self.status = "off"
		return self.status

	def ftp_on(self):
		done = 0
		if self.status == "on":
			done = 1
		else:
			run(["sudo", "launchctl", "load", "-w", self.path], capture_output=True)
			self.status = "on"
		return done
			
	def ftp_off(self):
		done = 0
		if self.status == "off":
			done = 1
		else:
			run(["sudo", "launchctl", "unload", "-w", self.path], capture_output=True)
			self.status = "off"
		return done

	def ftp_add_alias(self):
		alias = [
			"\n## - alias ftpd.py tool added\n"
			"alias ftpdon='sudo launchctl load -w /System/Library/LaunchDaemons/ftp.plist'\n",
			"alias ftpdoff='sudo launchctl unload -w /System/Library/LaunchDaemons/ftp.plist'\n",
			"alias ftpdstatus='sudo launchctl list | fgrep -i com.apple.ftpd'\n"
		]
		
		with open(self.path_profile, "a") as f:
			f.writelines(alias)
		with open(self.path_bashrc, "a") as f:
			f.writelines(alias)

