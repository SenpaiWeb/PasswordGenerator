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
if(len(sys.argv)>=2):
    label = sys.argv[1]
    for cnt,arg in enumerate(sys.argv):
        if arg == "--purge-output":
            open(savepath, "w").write("")
            exit()
        if arg == "--not-save":
            save = False
        elif arg == "-l":
            try:
                    length = int(sys.argv[cnt+1])
            except:
                print("Could not understand length, set to: "+str(length))
else:
    print("error while executing, correct usage is following: py "+sys.argv[0]+" <label> [-l <length>] [--not-save]")
    exit()
with open(savepath, "a+") as passesFile:
    passesFile.seek(0,0)
    readFile = passesFile.read()
    if((label + ":") not in readFile):
        urand = str(os.urandom(length)).replace("<", "!")
        md5 = hashlib.md5(urand.encode("utf-8")).hexdigest()[:length]
        if save:
            passesFile.write("\n"+label+":"+md5)
    else:
        md5 = re.search(label+":(.+)",readFile).group(1)
os.system("echo "+md5+"|clip")
print("Set to clipboard! ["+md5+"]")
