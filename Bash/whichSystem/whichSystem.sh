#!/bin/bash

function ctrl_c(){
	echo -e "\n[!]Saliendo\n"
	exit 1
}

function ttl(){
	trap ctrl_c INT

	echo -e "\n"
	echo -e "[*]Host -> " | tr -d '\n'
	read network
	
	ping=("ping -c 1")
	bash -c "$ping $network" >> ttl0
	cat ttl0 | grep ttl | awk '{print$6}' >> ttl1 
	cat ttl1 | tr -d '=,ttl' >> ttl2

}

function loop(){

	linuxint="63"
	windowsint="127"

	linuxttl=("[*]System -> Linux")
	windowsttl=("[*]System -> Windows")

	ttloop=$(while read line; do echo -e "$line"; done < ttl2)
	if [[ $ttloop == $linuxint ]]; then
		echo  "$linuxttl"

	elif [[ $ttloop == $windowsint ]]; then
		echo "$windowsttl"

	fi

}

function delete(){
        rm -r ttl0
        rm -r ttl1
        rm -r ttl2
}

ttl
loop
delete
