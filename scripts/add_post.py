from callback import callback
from add_new import *
import db
import create_file

"""
Created for the purpose of batch mode
"""
def add_post_(post_name,cat_name,tags="",status="wip"):
    #@db.cursor
    #def get_cat_dir(cat,**kwargs):
    #    res = kwargs["con"].execute("""
    #    select directory from categories where name =?
    #    """,(cat,))
    #    res= list(res)
    #    if len(res)==0:
    #        return "/"
    #    return res[0][0]
    cat_dir =  db.get_cat_dir(cat_name)
    #Create file before inserting into the database
    create_file.new_file(post_name,cat_dir)
    #Insert file into the database
    db.insert_post(post_name,cat_name,tags=tags,status=status)

@callback
def add_post(ctx,param,value,batch_mode=False,*args):
    if batch_mode:
        add_post_(*args)
    else:
        ask = Select_cat_add()
        ask.run()
        res = ask.result
        add_post_(res["post_name"],res["cat_name"])

