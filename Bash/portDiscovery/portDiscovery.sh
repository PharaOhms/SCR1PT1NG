#!/bin/bash

function ctrl_c(){
	echo -e "\n[!]Exit"
	exit 1
}

function portDiscovery(){
	trap ctrl_c INT

	echo -e "\n"
	echo -e "[*]Host -> " | tr -d '\n'
	read host

	echo -e "[+]Port Discovery"

	for port in $(seq 1 65535); do
	        bash -c "echo ' ' > /dev/tcp/$host/$port" 2>/dev/null && echo -e "\t[*] Port $port -> Open"  &
	done; wait
}

portDiscovery
