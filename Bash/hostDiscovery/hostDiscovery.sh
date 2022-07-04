#!/bin/bash

function ctrl_c(){
	echo -e "\n[!]Exit"
	exit 1
}

function host(){
	trap ctrl_c INT
	echo -e "\n"
	echo -e "[*]Host -> " | tr -d '\n'
	read host


	hostname=("$host")
	echo $hostname | grep -oP '\d{1,3}\.' | tr -d '\n',"" >> treatmentHost
  treatmentHost="$(cat treatmentHost)"

}

function loop(){

	trap ctrl_c INT

	
	initHost="$(cat treatmentHost)"
	segment="0/24"
  echo -e "[+]Host Discovery $treatmentHost$segment \n"

	for host in ${initHost[@]}; do
		 for x in $(seq 1 254); do
			 timeout 1 bash -c "ping -c 1 $initHost$x" &>/dev/null && echo -e "\t[*] Host $initHost$x -> Active" &
		 done; wait
	done
}

function delete(){
	rm -r treatmentHost
}

host
loop
delete
