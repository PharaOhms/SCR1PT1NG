#!/usr/bin/env python3
#Hexadecimal Converter

import time

def converter():
    hex= input("\nInput hexadecimal number >> ")
    decode= int(hex, 16)
    print("\nConvert {} in process".format(hex))
    time.sleep(1)
    print ("\n [*] Port {} [*] \n".format(decode))

converter()

def add():
    while True:
        add=input("Do you want add more values? [y] or [n] >> ")
        if add != "y" and add != "n":
            print("\nThe answer is not valid, please choice [y] or [n]\n")
        elif add == "y":
            converter()
        elif add == "n":
            print ("Killing Process, byeee!\n")
            break
add()
