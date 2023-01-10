import sqlite3
from collections import defaultdict


"""
Simple decorators to prevent writing boilerplate.
Use:
    @cursor
    def get_status_list(*kwargs):
    
        row =kwargs["con"].execute('select value from status_enum')
    
        return row
        
Instead of:


    def get_status_list():
        con = sqlite3.connect('db/web.sqlite3')
        cur = con.cursor()
    
        row = sorted([x[0] for x in cur.execute('select value from status_enum')])
    
        con.commit()
        con.close()
        return row
"""
def cursor(func):
    def inner(*args):
        con = sqlite3.connect('db/web.sqlite3')
        cur = con.cursor()

        res = func(*args,con=con)
    
        con.commit()
        con.close()
        return res
    return inner


def get_status_list():
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    row = sorted([x[0] for x in cur.execute('select value from status_enum')])

    con.commit()
    con.close()
    return row

def get_categories(filt=False):
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    row = cur.execute('select * from categories')
    
    if filt: 
        row = filter(lambda x: x[1] not in {"contact"},
                row)

    row = list(row)
    con.commit()
    con.close()
    return row

def get_file_of_post(post):
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    cat = list(cur.execute('select category from posts where name=?',(post,)))[0][0]
    index_file = list(cur.execute('select directory from categories where name=?',(cat,)))[0][0]

    con.commit()
    con.close()
    return index_file+post+".md"


def get_categories_map():
    return defaultdict(lambda:"Error",{x[1]:x[3] for x in get_categories()})

def get_tags_from_post_name(post):
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    row = list(cur.execute('select tags from posts where name=?',(post,)))

    con.commit()
    con.close()
    return row


def get_status_from_post_name(post):
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    row = list(cur.execute('select status from posts where name=?',(post,)))[0][0]

    con.commit()
    con.close()
    return row

def get_tags():
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    row = list(cur.execute('select tags from posts where not tags=""'))
    tags = set()
    for batch in row:
        t = batch[0].split("/")
        for st in filter(lambda x:len(x)!=0,t):
            tags.add(st)

    con.commit()
    con.close()
    return sorted(list(tags))

@cursor
def get_posts(**kwargs):
    row = list(kwargs["con"].execute('select * from posts'))
    return row

def listed_from_path(path):
    sep = path.split("/")
    cat = "_".join(sep[1:-1])
    name = sep[-1].split(".")[0]
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    row = list(cur.execute('select * from posts where category=? and name=?',
            (cat,name,))
            )

    con.commit()
    con.close()
    return len(row)>0



@cursor
def get_cat_dir(cat,**kwargs):
    res = kwargs["con"].execute("""
    select directory from categories where name =?
    """,(cat,))
    res= list(res)
    if len(res)==0:
        return "/"
    return res[0][0]



def add_category(name, index_file,directory):
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    con.execute("""
    insert into categories(name, index_file,directory) values(?,?,?)
    """,
    (name, index_file,directory,)
    )

    con.commit()
    con.close()
    print("Category added")

#def insert_post(name,path,category=""):
def insert_post(name,cat,tags="",status="wip"):
    #cat="/".join(path.split("/")[1:-1])
    #cat = cat.replace("/","_")
    #print(name,cat)

    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    try:
        row = list(cur.execute(
            'insert into posts(category,name,status,tags) values(?,?,?,?)',
            (cat,name.split(".")[0],status,tags)
            ))

#        print("Inserted!")
    except :
        print("Couldn't insert post")
        print("There was an error! Check you code. Dude!")
        row = list(cur.execute(
            'insert into posts(category,name,status,tags) values(?,?,?,?)',
            (cat,name.split(".")[0],status,tags)
            ))
    finally:
        con.commit()
        con.close()

def remove_category(id):
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    con.execute("""
    delete from categories where name=?
    """
    ,(id,)
    )

    con.commit()
    con.close()
    print("Category removed")

@cursor
def delete_post_by_name(name,**kwargs):
    kwargs["con"].execute("""
            delete from posts where name=?
            """,(name,))

def update_tags_from_post(post,tags):
    up = "/".join(sorted(tags))
    
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    con.execute("""
    update posts set tags=? where name=?
    """,
    (up, post,)
    )

    con.commit()
    con.close()

def update_status_from_post_name(post,status):
    con = sqlite3.connect('db/web.sqlite3')
    cur = con.cursor()

    row = cur.execute('update posts set status=? where name=?',(status,post,))

    con.commit()
    con.close()
