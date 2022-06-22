import time
import os

def dirTreatment():

    print("[+]Welcome to dirTreatment v1 by @pharaohms.")
    file = input("Insert file > ")

    command = ("bat " + (file) + " | awk '{print$9}' >> file.txt """)
    command2 = ("""bat file.txt | tr -d ' "" ',"" >> file2.txt """) 
    command3 = ('bat file2.txt | while read line; do echo "/$line"; done >> Directories')
    command4 = ("bat Directories")
    
    delete = ("rm -r file.txt file2.txt")

    time.sleep(1)
    InvokeCommand = os.system(command)
    InvokeCommand = os.system(command2)
    InvokeCommand = os.system(command3)
    InvokeCommand = os.system(command4)
    InvokeCommand = os.system(delete)

dirTreatment()
