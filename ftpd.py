#!/usr/bin/env python3
#
#	Author:		Antonio Perrucci
#	Company:	Magellano srl (Apulia - Brindisi)
#	Date:		02/05/2023 
#
#	Purpose:	enable / disable ftpd on MacOS
#	
#	URL:		https://github.com/antogit-sys/ftpd-macos.git
#	LICENSE:	GPLv3
#
##### BEGIN

import os
import sys
from time import sleep
import ftp_management as ftpm

def main(argc, argv):
	NAME = sys.argv[0]
	done = 0
	if argc == 1:
		helper(NAME)
	elif argc == 2:
		if not isRoot():
			print(NAME+": only root can run this script\n")
			done = -1
		else:
			fm = ftpm.ftpMan()
			print_init(NAME,"=")
			if fm.isFile:
				OP = argv[1]
				if OP == "status":
					print(" ftpd status ~> "+fm.ftp_status())
				
				elif OP == "on":
					if fm.ftp_on() == 0: 
						print(" ftpd is now enabled")
					else: print(" ftp is already ON")
				
				elif OP == "off":
					if fm.ftp_off() == 0:
						print(" ftpd is now disabled")
					else: print(" ftp is already OFF")
				
				elif OP == "alias":
					print("add alias ftp in:")
					print("\t"+fm.path_profile)
					print("\t"+fm.path_bashrc)
					fm.ftp_add_alias()
				else:
					print("operation not allowed, use on/off/status/alias")
					done = -1
			else:
				print("[!] ftp.plist daemon not found")
				sleep(1)
				print("ftp.plist Download && Install ...")
				sleep(2)
				fm.download_plist()
				print("\n"+NAME+": run the following script again!!!")
	return done

def helper(NAME):
	print(NAME+":")
	print("\tsimple script to on/off or see the status of ftp server")
	print("usage:")
	flag = ""	
	if "./" not in NAME:
		flag = "python3 "
	NAME = flag+NAME
	print("\t"+NAME+" [status|on|off|alias]")
	print("example:")
	print("\t"+NAME+" on")
	print("\t"+NAME+" status")
	print("\t"+NAME+" alias\n")
	print("\talias list:")
	print("\t\tftpdstatus --> status server ftp")
	print("\t\tftpdon --> ftpd set on")
	print("\t\tftpdoff --> ftpd off")


def isRoot():
	done = 0
	if os.geteuid() == 0:
		done = -1
	return done

def print_init(NAME, c):
	print(NAME)
	print(c*len(NAME))
	

if __name__ == "__main__":
	sys.exit(main(len(sys.argv), sys.argv))
