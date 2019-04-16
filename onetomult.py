#!/usr/bin/python3
import argparse, os, subprocess, fnmatch,sys,platform
arg=argparse.ArgumentParser()
arg.add_argument("dir", type=str, help="Directory that contains target files")
arg.add_argument("src",type=str, help="Source file")
arg.add_argument("--mask", "-m", type=str, help='Mask to choose files from')
args=arg.parse_args()
if args.mask!=None and args.mask!="" and args.mask!=" ":
    mask=args.mask
else:
    mask=None
onlyfiles = [f for f in os.listdir(args.dir) if os.path.isfile(os.path.join(args.dir, f))]
filtered=[]
if mask!=None:
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, mask):
            filtered.append(file)

else:
    filtered=onlyfiles
commandout=[]
for i in range(1,len(filtered)):
    if platform.system=="Windows":
        a=list(subprocess.getstatusoutput("copy /F "+args.src+" "+filtered[i]))
    else:
        a=list(subprocess.getstatusoutput("cp -vf "+args.src+" "+filtered[i]))
    if a[0]!=0:
        print(a[1])
        raise UserWarning("Error occurred.\n Abort, Retry or Skip? ")
        userinput = input()
        if userinput=="A" or userinput=="a":
            sys.exit(1)
        if userinput=="S" or userinput=="s":
            i+=1
    else:
        i+=1
commandout.append(a)
