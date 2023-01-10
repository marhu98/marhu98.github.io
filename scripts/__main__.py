#!/usr/bin/env python3

import create_file
import time
import re
from os.path import exists
import os
import sqlite3
import click
import db
from add_new import *
from collections import defaultdict
from callback import callback
from add_post import add_post
from add_cat import add_cat
from edit import edit
from new_post import new
from trash import trash
from delete import delete
from delete import remove

cwd = os.getcwd()
if "scripts" not in cwd:
    cwd = cwd+"scripts/"


###"""
###Edit draft
###"""
###@callback
###def edit(ctx,param,value):
###    ##click.echo("Editing {}".format((param,value)))
###    screen=Select_edit()
###    screen.run()
###    #click.echo("Go result")
###    #click.echo(screen.tag_result)
###
###   # if screen.result[1]==0:
###   #     file_ = db.get_file_of_post(screen.result[0][1])
###   #
###   #     os.system(f"$EDITOR static/{file_}")
###   #    #os.command("vim")
###   # elif screen.result[1]==1:
###   #     print("Editing tags")
###   #     screen_=Select_tags()
###   #     screen_.setup(screen.result[0][1])
###   #     screen_.run()
###   #     click.echo("Testing")
###   #     click.echo(screen_.result)


###"""
###Creates new post
###"""
###@callback
###def new(ctx,param,value):
###    screen = Add_new()
###    screen.run()
###    click.echo(screen.result)
###    """
###    Here there should be a check that the name is valid.
###    E.g: It doesn't contain invalid characters such as / or end already in .md
###    """
###
###
###    selected = screen.result["category"]
###    filename=screen.result["total_categories"][selected][3]+screen.result["name"]+".md"
###    click.echo(filename)
###
###    click.echo("Checking file doesn't already exist...")
###    if exists(filename):
###        click.echo("File already in use! Changing to edit")
###        edit(ctx,param,value)
###    else:
###        click.echo("New file has been created and added to the database")
###        template = f'{result["name"]}.md'
###        #print(f"cp ../templates/{template} ../static/{filename}")
###
###
###        os.system(f"cp ../templates/{template} ../static/{filename}")

#"""
#Created for the purpose of batch mode
#"""
#@db.cursor
#def trash_(post_name,**kwargs):
#    kwargs["con"].execute("""
#            update posts set status=? where name=?
#            """,("trash",post_name,))


###"""
###Moves post to trash "folder".
###I.e it applies the trash tag
###"""
###@callback
###def trash(ctx,param,value):
###    screen = Select_post()
###    screen.run()
###    #trash_(screen.result["name"])
###    db.update_status_from_post_name(screen.result["name"],"trash")


#"""
#Created for the purpose of batch mode
#"""
#@db.cursor
#def delete_(post_name,**kwargs):
#    kwargs["con"].execute("""
#            delete from posts where name=?
#            """,(post_name,))

###"""
###deletes post forever
###"""
###@callback
###Def delete(ctx,param,value):
###    screen = Select_post()
###    screen.run()
###    #delete_(screen.result["name"])
###    db.delete_post_by_name(screen.result["name"])

@callback
#@db.cursor
def list_(ctx,param,value,**kwargs):

    click.echo(f"Categories")
    click.echo("")
    cats = db.get_categories()
    for row in cats:
        click.echo(f"Name: {row[1]}\t Index file located at: {row[2]}")

    click.echo(f"Posts")
    click.echo("")
    posts=db.get_posts()
    #posts=kwargs["con"].execute("""
    #select * from posts
    #""")
    for row in posts:
        click.echo(f"Name: {row[2]}\t Status: {row[3]}")

###"""
###Created for the purpose of batch mode
###"""
###def add_cat_(cat_name,index_file,category_dir=""):
###    fail = False
###    #Check that the strings are well formed
###    if not category_dir=="" and not re.match("[\w/]+/$",category_dir):
###       print("Category directory is not well formed (make sure it ends in /)")
###       fail=True
###    if not re.match("\w+$",index_file):
###       print("Index file name is not well formed (make sure you don't include the extension)")
###       fail=True
###    pattern = re.search("^\w[\w\s]*$",cat_name)
###    if not pattern:
###       print("Category name is not well formed (make sure there are no weird characters, underscores are allowed)")
###       fail=True
###
###    if fail:
###        return
###
###    index_file=category_dir+index_file+".md"
###    #print(cat_name,index_file,category_dir)
###
###    db.add_category(pattern.group(),index_file,category_dir)
###
###@callback
###def add_cat(ctx,param,value):
###    screen = Add_cat()
###    screen.run()
###    result = screen.result
###    print(*result)
###
###    add_cat_(*result)

###"""
###Created for the purpose of batch mode
###"""
###def add_post_(post_name,cat_name,tags="",status="wip"):
###    #@db.cursor
###    #def get_cat_dir(cat,**kwargs):
###    #    res = kwargs["con"].execute("""
###    #    select directory from categories where name =?
###    #    """,(cat,))
###    #    res= list(res)
###    #    if len(res)==0:
###    #        return "/"
###    #    return res[0][0]
###    cat_dir =  db.get_cat_dir(cat_name)
###    #Create file before inserting into the database
###    create_file.new_file(post_name,cat_dir)
###    #Insert file into the database
###    db.insert_post(post_name,cat_name,tags=tags,status=status)
###
###@callback
###def add_post(ctx,param,value,batch_mode=False,*args):
###    if batch_mode:
###        add_post_(*args)
###    else:
###        ask = Select_cat_add()
###        ask.run()
###        res = ask.result
###        add_post_(res["post_name"],res["cat_name"])


###def remove_(cat):
###    db.remove_category(result)
###
###@callback
###def remove(ctx,param,value,batch_mode=False,*args):
###    if batch_mode:
###        remove_(*args)
###    else:
###        screen = Select_cat()
###        screen.run()
###        remove_(screen.result)

@callback
def init(ctx,param,value):
    click.echo("Not implemented yet")


@callback
def test(ctx,param,value):
    click.echo("Testing")
    @db.cursor
    def testy(**kwargs):
        row = kwargs["con"].execute("select * from posts where status='publish' order by date desc")
        row = map(lambda x:print(x), row)
        row = list(row)
    testy()


@callback
def batch(ctx,param,value):
    click.echo("Not implemented")

    with open(value,"r") as file:
        for line in file.readlines():
            #Test command is well formed
            cmds = ["add","update","delete","trash","remove"]
            reg_cmds=f'({("|").join(cmds)})'

            line = line.replace("\n","")
            match=re.match(f"(?P<cmd>{reg_cmds})\s+(?P<type>\w+)\s+(?P<tail>(\w+=[\w/]+\s?)+)$",
                    line)
            #match=re.search(f"\w+=\w+",
            #        line)

            if match==None:
                click.echo("Error, incorrect command found: {}".format(line))
            else:
                dic = defaultdict(lambda :"",match.groupdict())
                options = defaultdict(lambda:"",{x.split("=")[0]:x.split("=")[1] for x in dic["tail"].split(" ")})
                options["status"]=options["status"] if options["status"] else "wip"
                #click.echo(line)
                #click.echo(options)

                if dic["cmd"]=="add":
                    if dic["type"]=="post":
                        add_post_(options["name"],options["cat"],tags=options["tags"],status=options["status"])
                    elif dic["type"]=="cat":
                        add_cat_(options["name"],options["index"],category_dir=options["dir"])
                else:
                    click.echo(f"{dic['cmd']} not implemented yet")


@callback
@db.cursor
def ls(ctx,param,value,**kwargs):
    pass

@click.command()
@click.option('--init', is_flag=True, callback=init,is_eager=True,help="Set's up blog")
@click.option('-e','--edit', is_flag=True, callback=edit,is_eager=True,help="Edits post, eg: Add tags")
@click.option('-n','--new', is_flag=True, callback=new,is_eager=True,help="Creates new post")
@click.option('--trash', is_flag=True, callback=trash,is_eager=True,help="Sends post to the trash")
@click.option('-d','--delete', is_flag=True, callback=delete,is_eager=True,help="Deletes selected post")
@click.option('--list', is_flag=True, callback=list_,is_eager=True,help="Lists all categories/posts available at the moment",default=False)
@click.option('--add-cat', is_flag=True, callback=add_cat,is_eager=True,help="Adds new category")
@click.option('-a', '--add', is_flag=True, callback=add_post,is_eager=True,help="Adds new post")
@click.option('--remove-cat', is_flag=True, callback=remove,is_eager=True,help="Removes selected category")
@click.option('--test', is_flag=True, callback=test, is_eager=True,help="Runs preselected test. Remove on production,")
@click.option('-b','--batch',callback=batch,is_eager=True, help="Batch mode, runs commands inputed from a file")
@click.option('--ls',callback=ls,is_eager=True, help="Lists everything in the database")
def main(edit,new,trash,delete, add, init, *args,**kwargs):
    click.echo(cwd)
    click.echo("""Usage: scripts [OPTIONS]

Options:
  --init        Set's up blog
  -e, --edit    Edits post, eg: Add tags
  -n, --new     Creates new post
  --trash       Sends post to the trash
  -d, --delete  Deletes selected post
  --list        Lists all categories/posts available at the moment
  --add-cat     Adds new category
  -a, --add     Adds new post
  --remove-cat  Removes selected category
  -t            Runs preselected test. Remove on production,
  --batch TEXT  Batch mode, runs commands inputed from a file
  --help        Show this message and exit.        """)


"""
Creates database in case it doesn't already exist
"""
def init_database(database_name="db/web.sqlite3"):
    if not os.path.exists(database_name):
        print("Database doesn't exist, creating...")
        with open(database_name,"w"):
            print("File created")

        con = sqlite3.connect(database_name)
        cur = con.cursor()

        con.execute("""
        CREATE TABLE IF NOT EXISTS categories(
        id integer primary key autoincrement,
        name text not null unique,
        index_file text not null unique, directory text)
        """
        )
        con.execute("""
        CREATE TABLE IF NOT EXISTS sqlite_sequence(name,seq)
        """
        )
        con.execute("""
        CREATE TABLE IF NOT EXISTS status_enum(value text not null unique);
        """
        )
        con.execute("""
        CREATE TABLE IF NOT EXISTS "posts"(id integer primary key autoincrement,
        category text,name text unique,
        status text, tags text default "",
        date datetime default current_timestamp,
        last_update datetime default "",
        foreign key(category) references categories(name),
        foreign key(status) references status_enum(value)
        )
        """
        )
        #This is ment for the trigger
        con.execute("""
        CREATE TRIGGER IF NOT EXISTS last_update_time after update on posts
        BEGIN
        UPDATE posts SET last_update=datetime('NOW') WHERE id=NEW.id;
        END;
        )
        """
        )

        con.commit()
        con.close()

    else:
        print("Database already exists. Doing nothing")


if __name__=="__main__":
    #init_database()
    main()
