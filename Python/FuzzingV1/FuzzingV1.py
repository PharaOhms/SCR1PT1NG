import os
import time

time.sleep(1)

print("\nWelcome to Fuzzing v1.0 By @pharaohms.\n")
print("Requirements:\n"
"\n[+]Wfuzz\n"
"[+]Gobuster\n")

 
##FUZZING WITH DIRECTORY-LIST-LOWERCASE-2.3-MEDIUM.TXT
def DirMedium():
    wfuzz = "wfuzz -c -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt --hc 404 "
    target = input("\nIP Target > ")
    fuzz = "/FUZZ 2>/dev/null"
    command = (wfuzz + target + fuzz)
    print ("\nFuzzing Directories {} \n".format(target))
    InvokeCommand = os.system(command)
    
#DirMedium()

##FUZZING WITH BIG.TXT
def DirBig():
    wfuzz = "wfuzz -c -w /usr/share/wordlists/dirb/big.txt --hc 404 " 
    target = input("\nIP Target > ")
    fuzz = "/FUZZ 2>/dev/null"
    command = (wfuzz + target + fuzz)
    print ("\nFuzzing Directories {} \n".format(target))
    InvokeCommand = os.system(command)

#DirBig()


##FUZZING WITH EXTENSIONS-BIG.TXT
def BigExtensions():
    wfuzz = "gobuster dir -w /usr/share/wordlists/dirb/big.txt -u "
    target = input("\nIP Target > ")
    fuzz = " -x php,html,js,txt 2>/dev/null"
    command = (wfuzz + target + fuzz)
    print ("\nFuzzing Extensions {} \n".format(target))
    InvokeCommand = os.system(command)

#BigExtensions()

##FUZZING SUBDOMAINS WITH subdomains-top1million-20000.txt
def SubDomains():
    wfuzz = "wfuzz -c -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-20000.txt --hc 400,404 -t 50 "
    target = input("\nIP Target > ")
    host = ('-H "Host: FUZZ.{}"'.format(target))
    url = "-u http://{}".format(target)
    command = (wfuzz + host + url)
    print("\nFuzzing SubDomains\n")
    InvokeCommand = os.system(command)

#SubDomains()

##CALL START FUNCTION
##IF YOU CHOICE [0] ALL, YOU CAN PASS AT THE NEXT STEP WITH CTRL + C##
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
        "\n[1] directory-list-lowercase-2.3-medium.txt\n"
        "\n[2] big.txt\n"
        "\n>> ")
        if Wordlists == "1":
            return DirMedium()
        elif Wordlists == "2":
            return DirBig()
    elif startInput == "2":
        return SubDomains()
    elif startInput == "3":
        return BigExtensions()
    elif startInput == "0":
        return (DirMedium(),BigExtensions(),SubDomains(),DirBig())
    elif startInput == "Q" or startInput == "q":
        time.sleep(1)
        print("\n[+]Killing Process, Byee! \n")
        
startFuzz()

