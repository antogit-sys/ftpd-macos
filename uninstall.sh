#
# UNINSTALL ftpd.py
#
# -- costant
declare -r LGREEN='\033[1;92m'
declare -r RED='\033[1;31m'
declare -r LYELLOW='\033[1;33m'
declare -r LCYAN='\033[0;96m'
declare -r NC='\033[0m' # No Color


function main {
	essageBox
	execute
	
exit
}

messageBox() {
	dialog --backtitle "Setup uninstall ftpd.py (Magellano srl)" --title "FTPD Manager" \
	--msgbox "this tool is covered by the gpl3 license\n
		\ngithub: antogit-sys\n\n\n
		proceed with the uninstallation?..." \
	10 50
	clear
}

execute() {
	#- execute
	printf "${LYELLOW}uninstall FTPD Manager\n"
	echo -e "--------------------------${NC}"
	cd ..; sudo rm -rf ftpd-macos
	sudo rm /bin/ftpd
	printf "ftpd.py is... "
	sleep 1
	printf "${RED}deleted ${NC}\n"
	sleep 1
	printf "ftp_management.py is"
	printf "${RED}deleted${NC}\n"
	sudo rm /bin/ftp_management.py
	printf "${LGREEN}[!] END UNINSTALL${NC}\n"
}

main
