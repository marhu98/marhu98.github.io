import db
from glob import glob
import os
from termcolor import cprint
from collections import defaultdict
import click
from create_file import create_file

"""
Given a path of the form blog/etc
Returns the correct directory path and
the correct file in a zip form:

    Returns: (string,string) Correct directory, correct file path
"""
def dir_filepath(indexes):
    dirs = ("static/"+"/".join(index.split("/")[:-1])+"/" for index in indexes)
    correct_index = map(lambda x: "static/"+x,indexes)
    return zip(dirs,correct_index)

def get_name_from_path(path):
    return path.split("/")[-1]

#Solves the missing index problems
def fix_filepath(paths):
    dir_index = dir_filepath(paths)
    for (dir,index) in dir_index:
        #Checks if directory exists
        if not os.path.exists(dir):
            print(f"{dir} does not exist!. Creating:")
            os.makedirs(dir)

        #Creates file with proper extended markdown heading
        create_file(index,dir)

# Solves the problems detected by the integrity check
def fix(ctx,param,value):
    if not value or ctx.resilient_parsing:
        return
    result = check()

    if result["all right"]:
        click.echo("Nothing to fix!")
        return
    click.echo("Fixing")
    #Fix unexistent indexes
    if len(result["indexes"])!=0:
        #print(result["indexes"])
        fix_filepath(result["indexes"])
    #Fix unexistent files that appear listed on the database
    if len(result["unexistent"])!=0:
        fix_filepath(result["unexistent"])
    #Fix unlisted files that do in fact exsist
    if len(result["unlisted"])!=0:
        print(result["unlisted"])
        for file in result["unlisted"]:
            db.insert_post(get_name_from_path(file),file)
    ctx.exit()

#Current mishandling unexistent files
#Obvious since it never checks for file existance: What was I thinking?
def check(silent=True):
    #Check for missing index files:
    
    l_ = db.get_categories()
    l_dic = defaultdict(lambda:"Error",{x[1]:x[3] for x in l_})


    indexes = [x[2] for x in l_]
    dirs = [x[3] for x in l_]
    index_problem=[]
    
    for index in indexes:
        if index=="":
            continue
        if index=="index.md":
            if not os.path.exists(index):
                index_problem.append(index)
                if not silent:
                    cprint(f"Warning: Index Problem: {index} does not exist","red")
        else:
            if not os.path.exists("static/"+index):
                index_problem.append(index)
                if not silent:
                    cprint(f"Warning: Index Problem: {index} does not exist","red")

    post_dirs = set(["static/"+l_dic[x[1]] for x in db.get_posts()])
    listed = set([l_dic[x[1]]+x[2]+".md" for x in db.get_posts()])
    total = set()

    for d in post_dirs:
        for post in glob(f"{d}*.md"):
            if "index.md" in post:
                continue
            total.add(post)
    unlisted=total.difference(listed)
    unexistent = listed.difference(total)

    unexistent=set(
            filter(lambda x:not os.path.exists("static/"+x),unexistent
            ))
    unlisted=set(
            filter(lambda x:not db.listed_from_path(x),unlisted
            ))
    
    if not silent:
        list(map(lambda x: cprint(f"The file {x} is unlisted!","cyan","on_red"),unlisted))
        list(map(lambda x: cprint(f"The file {x} does not exists and should be created!","cyan","on_red"),unexistent))

    return {"indexes":index_problem, 
        "unlisted":unlisted,"unexistent":unexistent,
        "all right":len(unlisted)+len(unexistent)+len(index_problem)==0}

@click.command()
@click.option('-f','--fix', is_flag=True, callback=fix,is_eager=True,help="Fix posts")
def main(fix):
    result = check(silent=False)
    if result["all right"]:
        cprint("No problem in the files","green")
    else:
        cprint("\n")
        cprint("Some problems have been detected, use -f flag to fix them","green")


if __name__=="__main__":
    main()
