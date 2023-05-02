#!/usr/bin/env python3
#
#	Author:		Antonio Perrucci
#	Company:	Magellano srl (Apulia - Brindisi)
#	Date:		02/05/2023 
#
#	Purpose:	enable / disable ftpd on MacOS
#
#	URL:		https://github.com/antogit-sys/ftpd-macos.git
##### BEGIN

import os
import sys
import ftp_management as ftpm
from time import sleep

def main(argc, argv):
	NAME = sys.argv[0]
	#PLIST = '/System/Library/LaunchDaemons/ftp.plist'
	#PLIST = "prova"
	if argc == 1:
		helper(NAME)
	elif argc == 2:
		if not isRoot():
			print(NAME+": only root can run this script\n")
		else:
			fm = ftpm.ftpMan()
			if fm.isFile:
				OP = argv[1]
				if OP == "status":
					print(fm.getStatus())
					pass #ftp_status()
				elif OP == "on":
					pass #ftp_on()
				elif OP == "off":
					pass #ftp_off()
				else:
					print(NAME+": operation not allowed, use on/off/status")
			else:
				print(NAME+": ftp.plist daemon not found")
				sleep(1)
				print("ftp.plist Download && Install ...")
				sleep(2)
				fm.download_plist()
				print(NAME+": run the following script again!!!")
def helper(NAME):
	print(NAME+":")
	print("\tsimple script to on/off or see the status of ftp server")
	print("usage:")
	flag = ""	
	if "./" not in NAME:
		flag = "python3 "
	NAME = flag+NAME
	print("\t"+NAME+" [status|on|off]")
	print("example:")
	print("\t"+NAME+" on")
	print("\t"+NAME+" status")

def isRoot():
	done = 0
	if os.geteuid() == 0:
		done = -1
	return done

def isFile(path):
	return os.path.isfile(path)

if __name__ == "__main__":
	sys.exit(main(len(sys.argv), sys.argv))
