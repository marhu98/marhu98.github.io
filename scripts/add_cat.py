from callback import callback
from add_new import *
import db
import create_file
import re

"""
Created for the purpose of batch mode
"""
def add_cat_(cat_name,index_file,category_dir=""):
    fail = False
    #Check that the strings are well formed
    if not category_dir=="" and not re.match("[\w/]+/$",category_dir):
       print("Category directory is not well formed (make sure it ends in /)")
       fail=True
    if not re.match("\w+$",index_file):
       print("Index file name is not well formed (make sure you don't include the extension)")
       fail=True
    pattern = re.search("^\w[\w\s]*$",cat_name)
    if not pattern:
       print("Category name is not well formed (make sure there are no weird characters, underscores are allowed)")
       fail=True

    if fail:
        return

    index_file=category_dir+index_file+".md"
    #print(cat_name,index_file,category_dir)

    db.add_category(pattern.group(),index_file,category_dir)

@callback
def add_cat(ctx,param,value):
    screen = Add_cat()
    screen.run()
    result = screen.result
    print(*result)

    add_cat_(*result)
