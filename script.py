import os
import io
import hashlib
# args: --not-save, -l(ength)
urand = str(os.urandom(12)).replace("<", "!")
md5 = hashlib.md5(urand.encode("utf-8")).hexdigest()
os.system("echo "+md5+"|clip")
print("Set to clipboard! ["+md5+"]")
