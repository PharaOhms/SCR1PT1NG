import time
import os
import sys


#BANNER
def banner():

    time.sleep(1)
    banner_user = (
    "\nWelcome To PortScanner v1 By @pharaohms\n"
    "Requirements: [+]nmap [+]extractPorts")
    print(banner_user)

##CHECK CONECTIVITY && SO
def ping():
    targetIP = input("\nInsert Target IP > ")
    command = ("ping -c 1 {} >> ping".format(targetIP))
    so = ("cat ping | head -n2 | awk '{print$6}' | grep -oP '\d{1,3}' >> ttl")
    ttl = ('echo [+]Receiving Ping && while read line; do echo "[+]ttl:$line" ; done < ttl')
    delete = ("rm -r ping ttl")
    InvokeCommand = os.system(command)
    InvokeCommand2 = os.system(so)
    time.sleep(1)
    InvokeCommand3 = os.system(ttl)
    InvokeCommand4 = os.system(delete)

    time.sleep(1)
    if InvokeCommand3 >= 0 and InvokeCommand3 <= 64:
        print("[+]Operating System > Linux\n")
        sys.exit(0)

    elif InvokeCommand3 >= 65 and InvokeCommand3 <= 128:
        print("[+]Operating System > Windows\n")
        sys.exit(0)


def target():
    
    command1 = ("extractPorts allPorts")
    InvokeCommand = os.system(command1)
    ports = input("\n[+]Insert Target Ports > ")
    ip_address = ("cat allPorts | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u | xclip -sel clip | echo '\n[*] IP Address copied to clipboard'")
    InvokeAddress = os.system(ip_address)
    address = input("\n[+]Insert Target IP > ")
    command2 = ("nmap -sC -sV -p{} {} -oN target").format(ports,address)
    print("\n[+]Scanning Version of Ports: {} in the Target: {}[+]\n".format(ports,address))
    InvokeCommand2 = os.system(command2)
    sys.exit(0)




##ALLPORTS
def allPorts():

    targetIP = input("\nInsert Target IP > ")
    command = ("nmap {} -p- --open -Pn -vvv -oG allPorts".format(targetIP))
    print ("\n[+]Scanning AllPorts of Target: {}[+]\n".format(targetIP))
    time.sleep(1)
    InvokeCommand = os.system(command)

##VERSION
def target():
    
    print("\n[+]Starting Scanning Version of allPorts[+]\n")
    command1 = ("extractPorts allPorts")
    InvokeCommand = os.system(command1)
    ports = input("\n[+]Insert Target Ports > ")
    ip_address = ("cat allPorts | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u | xclip -sel clip | echo '\n[*] IP Address copied to clipboard'")
    InvokeAddress = os.system(ip_address)
    address = input("\n[+]Insert Target IP > ")
    command2 = ("nmap -sC -sV -p{} {} -oN target").format(ports,address)
    print("\n[+]Scanning Version of Ports: {} in the Target: {}[+]\n".format(ports,address))
    time.sleep(1)
    InvokeCommand2 = os.system(command2)
    


##UDP
def Udp():
    udp_scan = input("\n[+]Insert IP > ")
    command = ("sudo nmap -sU  -v  {} -oN udpScan".format(udp_scan))
    print("\n[+]Scanning UDP Ports of Target: {} [+]\n".format(udp_scan))
    time.sleep(1)
    InvokeCommand = os.system(command)
    

##HOST DISCOVERY
def HostDiscovery():
    
    usage = ("\n[!]Please for use Host Discovery Replace the last dot of Target IP for a 0." 
    "\n[!]Example : (10.10.10.16 >> 10.10.10.0)\n")
    print(usage)
    targetHost = input("\n[+]Insert Host > ")
    command = ("nmap -sn  {}/24 -oN HostDiscovery".format(targetHost))
    print("\n[+]Discovery Hosts on Target : {}\n".format(targetHost))
    time.sleep(1)
    InvokeCommand = os.system(command)
    

    

##CALL STARTER FUNCTION
def startNmap():

    time.sleep(1)
    startInput = input("\n[*]Select Scanner Index\n"
    "\n[0] PING\n"
    "\n[1] [TCP allPorts]\n"
    "\n[2] [TCP targeted]\n"
    "\n[3] UDP\n"
    "\n[4] HOST DISCOVERY\n"
    "\n[q] Quit\n"
    "\n> ")

    if startInput == "Q" or startInput == "q":
        time.sleep(1)
        print("\n[*] Killing Process, Byee!\n")
    
    elif startInput == "0":
        return ping()

    elif startInput == "1":
        return (allPorts())
    
    elif startInput == "2":
        return target()

    elif startInput == "3":
        return Udp()

    elif startInput == "4":
        return HostDiscovery()

    else:
        print("\n[!]Usage 1, 2, 3, 4 or Q for exit.")
        return startNmap()


##CALLS
banner()
startNmap()
