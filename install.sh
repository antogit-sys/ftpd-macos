#
# INSTALL
#
# -- costant
declare -r LGREEN='\033[1;92m'
declare -r RED='\033[1;31m'
declare -r LYELLOW='\033[1;33m'
declare -r LCYAN='\033[0;96m'
declare -r NC='\033[0m' # No Color


function main {
	install_dependence
	messageBox
	execute
	
exit
}

install_dependence() {
	brew install dialog
	brew install python3
	python3 -m pip install pip
	pip3 install wget
	clear
}

messageBox() {
	dialog --backtitle "Setup install ftpd.py (Magellano srl)" --title "FTPD Manager" \
	--msgbox "this tool is covered by the gpl3 license\n
		\ngithub: antogit-sys\n\n\n
		proceed with the installation?..." \
	10 50
	clear
}

execute() {
	#- execute
	printf "${LYELLOW}install FTPD Manager\n"
	echo -e "--------------------------${NC}"
	printf "ftpd.py is... "
	sleep 1
	printf "${LGREEN}executable ${NC}\n"
	sudo chmod a+x ftpd.py
	printf "copy ftpd.py in... "
	sleep 1
	printf "${LGREEN}/bin/ftpd${NC}\n"
	sudo cp ftpd.py /bin/ftpd
	printf "copy module ftp_management.py in..."
	sleep 2
	printf "${LGREEN}/bin/ftp_management.py${NC}\n"
	sudo cp ftp_management.py /bin/ftp_management.py
	printf "${LCYAN}[!] END INSTALL${NC}\n"
}

main
