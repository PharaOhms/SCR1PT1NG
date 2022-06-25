#Import

import time
import os
import sys
import requests
from requests.exceptions import HTTPError

#Directories
def directories():
    try:
        
        protocol = ("https://")
        url = (sys.argv[1])
        slash = ("/")
        directory = (sys.argv[2])
        r = requests.get( protocol + url )
        rd = requests.get( protocol + url + slash + directory )


        print("\nChecking: {} \nStatus code: {}\n".format((sys.argv[1]), (r.status_code)))
        print("\nChecking: {}/{} \nStatus code: {}\n".format((sys.argv[1]), (sys.argv[2]), (rd.status_code)))

        print("[+]Header")

        print("[*]Powered By: {}".format(r.headers['x-powered-by']))
        print("[*]Hosted By: {}".format(r.headers['x-hosted-by']))
        print("[*]Server: {}".format(r.headers['Server']))
        print("[*]Content-Type: {}\n".format(r.headers['Content-Type']))

    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')

    except Exception as error:
        print(f'[!]{error} not found.\n')


#Headers
def headers():

    try:
        
        protocol = ("https://")
        url = (sys.argv[1])
        r = requests.get( protocol + url)

        print("[+]Header")

        print("[*]Powered By: {}".format(r.headers['x-powered-by']))
        print("[*]Hosted By: {}".format(r.headers['x-hosted-by']))
        print("[*]Server: {}".format(r.headers['Server']))
        print("[*]Content-Type: {}\n".format(r.headers['Content-Type']))

    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')

    except Exception as error:
        print(f'[!]{error} not found.\n')


#Status Code
def StatusCode():

    protocol = ("https://")
    url = (sys.argv[1])
    
    try:
        r = requests.get( protocol + url)
        print("\nChecking:{} \nStatus code: {}\n".format(sys.argv[1],r.status_code))
        
    
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')

    except Exception as error:
        print(f'[!]{error} not found.\n') 

    return headers()
    

#Starter
def starter():

    banner = ("\n[*]Welcome to req.py v1.0 By @pharaohms")
    print(banner)

    if len(sys.argv) < 2:
        print("[!]Usage python3 req.py google.com\n")

    elif len(sys.argv) == 2:
        return StatusCode()

    elif len(sys.argv) == 3:
        return directories()


if __name__ == "__main__":
    starter()
