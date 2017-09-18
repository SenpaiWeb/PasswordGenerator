import os
import io
import sys
import hashlib
import re
# usage: py generator.py <label>
# example: py generator.py facebook.com
save = True # do not touch
savepath = os.getcwd() + "\precious.info" # save path
length = 32 # length of the generated password
Show = False # do not touch
if(len(sys.argv)>=2):
    label = sys.argv[1]
    for cnt,arg in enumerate(sys.argv):
        if arg == "--purge-output":
            open(savepath, "w").write("")
            exit()
        elif arg == "-e":
            label = input("Label: ")
        elif arg == "--show":
            Show = True
        elif arg == "--not-save":
            save = False
        elif arg == "-l":
            try:
                    length = int(sys.argv[cnt+1])
            except:
                print("Could not understand length, set to: "+str(length))
else:
    print("error while executing, correct usage is following: py "+sys.argv[0]+" <label or -e> [-l <length>] [--not-save] [--show]")
    exit()
with open(savepath, "a+") as passesFile:
    passesFile.seek(0,0)
    readFile = passesFile.read()
    if((label + ":") not in readFile):
        urand = str(os.urandom(length)).replace("<", "!")
        password = hashlib.md5(urand.encode("utf-8")).hexdigest()[:length]
        if save:
            passesFile.write(label+":"+password+"\n")
    else:
        password = re.search(label+":(.+)",readFile).group(1)
os.system("echo "+password+"|clip")
if Show:
    print(password)
