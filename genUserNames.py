import os

with open("/usr/share/seclists/Usernames/Names/familynames-usa-top1000.txt","r") as f:
    lastNames = f.readlines()
with open("/usr/share/seclists/Usernames/Names/femalenames-usa-top1000.txt","r") as f:
    fNames = f.readlines()
with open("/usr/share/seclists/Usernames/Names/malenames-usa-top1000.txt","r") as f:
    mNames = f.readlines()

with open("/home/rm/genFemaleUsers","w") as fm:
    for i in fNames:
        for j in lastNames:
            line = "" + i[:-1] + "_" + j[:-1] + "\n"
            fm.write(line)

with open("/home/rm/genMaleUsers","w") as fn:
    for i in mNames:
        for j in lastNames:
            line = "" + i[:-1] + "_" + j[:-1] + "\n"
            fn.write(line)

