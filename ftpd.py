#!/usr/local/bin/python3 
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

def main(argc, argv):
	NAME = argv[0]
	if argc == 1:
		helper(NAME)
	elif argc == 2:
		OP = argv[1]
		if OP == "status":
			pass #ftp_status()
		elif OP == "on":
			pass #ftp_on()
		elif OP == "off":
			pass #ftp_off()
		else:
			print(NAME+": operation not allowed, use on/off/status")

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


if __name__ == "__main__":
	sys.exit(main(len(sys.argv), sys.argv))
