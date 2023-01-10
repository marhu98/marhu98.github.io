from glob import glob
import os
from functools import reduce

path = ".."

subpaths= ["static/blog/**/*.md",
        "static/contact/*md","static/rants/**/*.md"]


files = map(lambda x:glob(f"{x}",recursive=True),subpaths)
files = reduce(lambda a,b:a+b,files)
files = list(filter(lambda x: "scrap" not in x, files))

for file in files:
    directory = file.split("/")[:-1]
    directory="/".join(directory)
    
#   Compile md (php) in static to md in bin
    directory = directory.replace("static","bin")
    binfile = file.replace("static","bin")
    newname=".".join(binfile.split(".")[:-1])+".md"
    #print(f"php {file} > {newname}")
    os.system(f"php {file} > {newname}")
    

#   Compile md in bin to md in html
    directory = directory.replace("bin","public")
#    if not os.path.exists(directory):
#        os.makedirs(directory)

    newfile = file.replace("static","public")
    newname=".".join(newfile.split(".")[:-1])+".html"
    os.system(f"pandoc --template bin/default.html5 -i {binfile} -o {newname}")
    #print(f"pandoc --template bin/default.html5 -i {binfile} -o {newname}")

os.system(f"pandoc --template bin/default.html5 -i index.md -o index.html")
#print(files)

