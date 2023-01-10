import os
import re

def create_file(filename,dir):
    if not os.path.exists(filename):
        name = filename.split("/")[-1][:-len(".md")]
        cap_name = name[0].upper()+name[1:]
        if cap_name=="Index":
            name = filename.split("/")[-2]
            cap_name = name[0].upper()+name[1:]
        print(f"{filename} does not exist. Creating")

        rep_dir=re.sub("\w+","..",dir)
        #print(f"Testing:{rep_dir}")
        heading=f"""---
title: {cap_name}                                                        
css:
- {rep_dir}style.css                
path: {rep_dir}
---

# {cap_name}"""
        if not os.path.exists(filename):
            with open(filename,"w") as file:
                file.write(heading)    


"""
Creates new file given:
    filename: test.md
    cat_dir: blog/math/
"""
"""
NOTE TO MYSELF: ALWAYS PUT WHAT THE FREAKING FUNCTION DOES
I can't remember what the one above does
"""
def new_file(filename,cat_dir):
    path = "static/"+cat_dir+filename+".md"
    print(filename)
    cap_name = filename[0].upper()+filename[1:]
    rep_dir=re.sub("\w+","..",cat_dir)+"../"
    if not os.path.exists(path):
        heading=f"""---
title: {cap_name}                                                        
css:
- {rep_dir}style.css                
path: {rep_dir}
---

# {cap_name}"""
        with open(path,"w") as file:
            file.write(heading)    
