from glob import glob
import os

bas_dir = "static"
dest_dir = ["bin","public"]

# First we get the tree directory from bas_dir

bas_set = set(filter(lambda x: "scrap" not in x and "escalada" not in x,map(lambda x:x[len("static/"):],glob("static/**/*/",recursive=True))))

clear = True
for origin in bas_set:
    for dest in  dest_dir:
        path = dest+"/"+origin
        if not os.path.exists(path):
            clear = False
            print(f"Not existent path detected! {path}. \n Creating!")
            os.makedirs(path)            

if clear:
    print("Everything is in order!")
