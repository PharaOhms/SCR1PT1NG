
#!/bin/bash

#Colours
greenC="\e[0;32m\033[1m"
endC="\033[0m\e[0m"
redC="\e[0;31m\033[1m"
blueC="\e[0;34m\033[1m"
yellowC="\e[0;33m\033[1m"
purpleC="\e[0;35m\033[1m"
turquoiseC="\e[0;36m\033[1m"
grayC="\e[0;37m\033[1m"

function ctrl_c(){
	echo -e "\n${yellowC}[!]Exit${endC}"
	exit 0
}

function host(){
	trap ctrl_c INT
	echo -e "\n"
	echo -e "[*]${blueC}Host${endC} -> " | tr -d '\n'
	read host


	hostname=("$host")
	echo $hostname | grep -oP '\d{1,3}\.' | tr -d '\n',"" >> treatmentHost
        treatmentHost="$(cat treatmentHost)"

}

function loop(){

	trap ctrl_c INT

	
	initHost="$(cat treatmentHost)"
	segment="0/24"
        echo -e "[+]${blueC}Host Discovery${endC} $treatmentHost$segment \n"

	for host in ${initHost[@]}; do
		for x in $(seq 1 254); do
			timeout 1 bash -c "ping -c 1 $initHost$x" &>/dev/null && echo -e "\t[*]${yellowC} Host $initHost$x ${endC}-> Active" &
		done; wait
	done
}

function delete(){
	rm -r treatmentHost
}

host
loop
delete
