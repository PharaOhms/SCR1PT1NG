import os
import time

time.sleep(1)

print("\nWelcome to Fuzzing v1.1 By @pharaohms.\n")
print("Requirements:\n"
"\n[+]Wfuzz\n"
"[+]Gobuster\n")



##FUZZING WITH DIRECTORY-LIST-LOWERCASE-2.3-SMALL.TXT
def DirSmall():

    wfuzz = "wfuzz -c -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt --hc 404 "
    print("\n[+] Protocol")
    targetSSL = input(
    "\n[1] HTTP"
    "\n[2] HTTPS\n"
    "\n>> ")

    targetIP = input("\n[+] IP Target > ")
    targetPort = input("[+] Port Target > ")
    fuzz = "/FUZZ 2>/dev/null"

    if targetSSL == "1":
        url = "http://{}:{}".format(targetIP,targetPort)
        command = (wfuzz + url + fuzz)
        print ("\nFuzzing Directories {}:{}\n".format(targetIP,targetPort))
        InvokeCommand = os.system(command)

    elif targetSSL ==  "2":
        url = "https://{}:{}".format(targetIP,targetPort)
        command = (wfuzz + url + fuzz)
        print("\nFuzzing directories {}:{}".format(targetIP,targetPort))
        InvokeCommand = os.system(command)

 

##FUZZING WITH DIRECTORY-LIST-LOWERCASE-2.3-MEDIUM.TXT
def DirMedium():

    wfuzz = "wfuzz -c -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt --hc 404 "
    print("\n[+] Protocol")
    targetSSL = input(
    "\n[1] HTTP"
    "\n[2] HTTPS\n"
    "\n>> ")

    targetIP = input("\n[+] IP Target > ")
    targetPort = input("[+] Port Target > ")
    fuzz = "/FUZZ 2>/dev/null"

    if targetSSL == "1":
        url = "http://{}:{}".format(targetIP,targetPort)
        command = (wfuzz + url + fuzz)
        print ("\nFuzzing Directories {}:{}\n".format(targetIP,targetPort))
        InvokeCommand = os.system(command)

    elif targetSSL ==  "2":
        url = "https://{}:{}".format(targetIP,targetPort)
        command = (wfuzz + url + fuzz)
        print("\nFuzzing directories {}:{}".format(targetIP,targetPort))
        InvokeCommand = os.system(command)

    
    
#DirMedium()

##FUZZING WITH BIG.TXT
def DirBig():

    wfuzz = "wfuzz -c -w /usr/share/wordlists/dirb/big.txt --hc 404 " 
    print("\n[+] Protocol")
    targetSSL = input(
    "\n[1] HTTP"
    "\n[2] HTTPS\n"
    "\n>> ")

    targetIP = input("\n[+] IP Target > ")
    targetPort = input("[+] Port Target > ")
    fuzz = "/FUZZ 2>/dev/null"

    if targetSSL == "1":
        url = "http://{}:{}".format(targetIP,targetPort)
        command = (wfuzz + url + fuzz)
        print ("\nFuzzing Directories {}:{}\n".format(targetIP,targetPort))
        InvokeCommand = os.system(command)

    elif targetSSL ==  "2":
        url = "https://{}:{}".format(targetIP,targetPort)
        command = (wfuzz + url + fuzz)
        print("\nFuzzing directories {}:{}".format(targetIP,targetPort))
        InvokeCommand = os.system(command)

#DirBig()


##FUZZING WITH EXTENSIONS-BIG.TXT
def BigExtensions():

    wfuzz = "gobuster dir -w /usr/share/wordlists/dirb/big.txt -u "
    print("\n[+] Protocol")
    targetSSL = input(
    "\n[1] HTTP"
    "\n[2] HTTPS\n"
    "\n>> ")

    targetIP = input("\n[+] IP Target > ")
    targetPort = input("[+] Port Target > ")
    fuzz = " -x php,html,js,txt 2>/dev/null"

    if targetSSL == "1":
        url = "http://{}:{}/".format(targetIP,targetPort)
        command = (wfuzz + url + fuzz)
        print ("\nFuzzing Extensions {}:{}\n".format(targetIP,targetPort))
        InvokeCommand = os.system(command)

    elif targetSSL ==  "2":
        url = "https://{}:{}/".format(targetIP,targetPort)
        command = (wfuzz + url + fuzz)
        print("\nFuzzing Extensions {}:{}".format(targetIP,targetPort))
        InvokeCommand = os.system(command)


#BigExtensions()

##FUZZING SUBDOMAINS WITH subdomains-top1million-20000.txt
def SubDomains():
    wfuzz = "wfuzz -c -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-20000.txt --hc 200,400,404 -t 50 "
    print("\n[+] Protocol")
    targetSSL = input(
    "\n[1] HTTP"
    "\n[2] HTTPS\n"
    "\n>> ")

    targetIP = input("\n[+] IP Target > ")
    targetPort = input("[+] Port Target > ")

    
    host = ('-H "Host: FUZZ.{}:{}"'.format(targetIP,targetPort))
    
    if targetSSL == "1":
        url = "-u http://{}:{}".format(targetIP,targetPort)
        command = (wfuzz + host + url)
        print ("\nFuzzing SubDomains {}:{}\n".format(targetIP,targetPort))
        InvokeCommand = os.system(command)

    elif targetSSL ==  "2":
        url = "-u https://{}:{}".format(targetIP,targetPort)
        command = (wfuzz + host + url)
        print("\nFuzzing SubDomains {}:{}".format(targetIP,targetPort))
        InvokeCommand = os.system(command)



##CALL START FUNCTION
def startFuzz():
    time.sleep(1)
    startInput = input("\nInsert Fuzzing Index: \n"
    "\n[0] All\n"
    "\n[1] Directory\n"
    "\n[2] SubDomains\n"
    "\n[3] Extensions\n"
    "\n[Q] Quit\n"
    "\n>> ")

    if startInput == "1":
        Wordlists = input("\nInsert Wordlist Index: \n"
        "\n[0] small.txt\n"
        "\n[1] medium.txt\n"
        "\n[2] big.txt\n"
        "\n>> ")
        if Wordlists == "1":
            return DirMedium()
        elif Wordlists == "2":
            return DirBig()
        elif Wordlists == "0":
            return DirSmall()
    elif startInput == "2":
        return SubDomains()
    elif startInput == "3":
        return BigExtensions()
    elif startInput == "0":
        return (DirMedium(),BigExtensions(),SubDomains(),DirBig())
    elif startInput == "Q" or startInput == "q":
        time.sleep(1)
        print("\n[+]Killing Process, Byee! \n")
    else:
        print("\n[+] Usage: 0, 1, 2, 3 or Q/q for exit.\n")
        return startFuzz()
        
startFuzz()
