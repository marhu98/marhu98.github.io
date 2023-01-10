import npyscreen

import os
from db import *
import numpy as np

def prepare_string(s):
    s = s.split("_")[-1]
    return s[0].upper()+s[1:]

class Add_new(npyscreen.NPSApp):

    def main(self):

        cap = lambda x:x[0].upper()+x[1:]

        values = get_categories()

        F = npyscreen.Form(name="Creating a new post",)
        t = F.add(npyscreen.TitleSelectOne, max_height=len(values), name="Category",value=[0,],
                values=[prepare_string(v[1]) for v in values[1:]],scroll_exit=True)
        
        fn = F.add(npyscreen.TitleText, name="Name of the post")
        F.edit()
        self.result = {"category":t.get_value()[0],"name":cap(fn.get_value()),
                "total_categories":values}

class Add_cat(npyscreen.NPSApp):

    def main(self):
        cap = lambda x:x[0].upper()+x[1:]

        values = get_categories()

        F = npyscreen.Form(name="Creating a new category",)
        
        f1 = F.add(npyscreen.TitleText, name="Name of the category")
        f2 = F.add(npyscreen.TitleText, name="Index file name",value="index")
        f3 = F.add(npyscreen.TitleText, name="Posts directory (leave blank for default). E.g:math/teach/")

        F.edit()
        self.result = [f1.get_value(),f2.get_value(),f3.get_value()]

class Select_cat(npyscreen.NPSApp):

    def main(self):

        cap = lambda x:x[0].upper()+x[1:]

        values = get_categories()

        F = npyscreen.Form(name="Select the category you wish to delete",)
        t = F.add(npyscreen.TitleSelectOne, max_height=len(values), name="Category",value=[0,],
                values=[prepare_string(v[1]) for v in values[1:]],scroll_exit=True)
        
        F.edit()
        #self.result = values[t.get_value()[0]][1]
        self.result = values[t.get_value()[0]+1][1]
        return
    


class New_post(npyscreen.NPSAppManaged):
    pass


class Select_cat_add(npyscreen.NPSApp):

    def main(self):

        cap = lambda x:x[0].upper()+x[1:]

        values = get_categories(filt=True)
        tags= get_tags()

        F = npyscreen.Form(name="Select the category of the post",max_height=3)
        post = F.add(npyscreen.TitleText, name="Enter the name of the post")
        cat = F.add(npyscreen.TitleSelectOne, max_height=len(values), name="Category (press control a to add categories)",value=[0,],
                values=[prepare_string(v[1]) for v in values[1:]],scroll_exit=True)
        tag = F.add(npyscreen.TitleMultiSelect, max_height=2*len(tags), name="Tags(press control t to add tags)",value=[],
                values=sorted([prepare_string(v) for v in tags]),scroll_exit=True)
        
        F.edit()
        #self.result = values[t.get_value()[0]][1]
        self.result = {"post_name":post.get_value(),
            "cat_name":values[cat.get_value()[0]+1][1],
            "tags":"/".join([tags[x] for x in tag.get_value()])}

tag_result ={}
class Select_edit(npyscreen.NPSAppManaged):

    def __init__(self):
        super().__init__()

        self.tag_result = tag_result 

    def onStart(self):
        self.addForm("MAIN",Select_edit_form,name="Select what you want to edit")
        self.addForm("SECOND",Select_tags_form,name="Select which tags do you want to be applied to the post")

    def change_form(self,name):
        self.switchForm(name)

    #def main(self):
    #    rep = lambda rep : " ".join(rep.split("_"))
    #    prep = lambda x: prepare_string(x)
    #    F = npyscreen.Form(name="Select what you want to edit",)
    #    #F = npyscreen.Form(name="Select what you want to edit",)
    #
    #    posts_ = [(x[1],x[2]) for x in get_posts()]
    #    posts = map(lambda x:(prep(x[0]),prep(x[1])),posts_)
    #    posts = list(map(lambda x:f"{x[1]} ({x[0]})",posts))
    #    a = F.add(npyscreen.TitleSelectOne, max_height=len(posts), name="Which post do you want to edit",
    #            value=[0,],values=posts,scroll_exit=True)

    #    b = F.add(npyscreen.TitleSelectOne, max_height=len(op)+2, name="Edit post or tags", value=[0,],values=op,scroll_exit=True)

    #    F.edit()
    #    #F.edit()

    #    self.result=[posts_[a.get_value()[0]],b.get_value()[0]]

class Select_edit_form(npyscreen.ActionForm):
    def setup_posts(self):
        rep = lambda rep : " ".join(rep.split("_"))
        prep = lambda x: prepare_string(x)
    
        posts_ = [(x[1],x[2]) for x in get_posts()]
        self.posts_=posts_
        posts = map(lambda x:(prep(x[0]),prep(x[1])),posts_)
        posts = list(map(lambda x:f"{x[1]} ({x[0]})",posts))
        return posts

    def create(self):
        posts = self.setup_posts()
        op = ["Edit text","Edit tags/status"]
        self.a = self.add(npyscreen.TitleSelectOne, max_height=len(posts), name="Which post do you want to edit",
                value=[0,],values=posts,scroll_exit=True)

        self.b = self.add(npyscreen.TitleSelectOne, max_height=len(op)+2, name="Post datum", value=[0,],values=op,scroll_exit=True)

    def on_ok(self):

        cat_name = self.posts_[self.a.get_value()[0]]
        post = cat_name[1]
        if self.b.get_value()[0]==0:
            name = cat_name[1]
            file_ = get_file_of_post(name)
            os.system(f"$EDITOR static/{file_}")
            self.parentApp.switchForm(None)
        else:

            self.tags = sorted(get_tags())

            self.selected = get_tags_from_post_name(post)[0][0]
            self.selected = self.selected.split("/")
            
            self.indexs = []

            for i,tag in enumerate(self.tags):
                if tag in self.selected:
                    self.indexs.append(i)

            self.parentApp.getForm("SECOND").post=post
            self.parentApp.getForm("SECOND").a.set_value(self.indexs)
            self.parentApp.getForm("SECOND").a.set_values(self.tags)
            self.parentApp.getForm("SECOND").a.max_height=len(self.tags)
            
            #Get the correct index for the status
            status =  get_status_from_post_name(post)
            index = filter(lambda x:x[1]==status,enumerate(self.parentApp.getForm("SECOND").status_list))
            index=list(index)[0][0]
            tag_result[index]=status
            self.parentApp.getForm("SECOND").b.set_value([index,])

            self.parentApp.switchForm("SECOND")

    def on_cancel(self):
        self.parentApp.switchForm(None)

class Select_tags_form(npyscreen.ActionForm):

    def create(self):

        self.tags=["If you're seening this there was a loading error",2,3]
        self.indexs=[1,]
        #self.setup(tag_result["name"])

        #self.f1 = self.add(npyscreen.TitleText, name="Tags")
        self.a = self.add(npyscreen.TitleMultiSelect, max_height=5, name="Which tags do you want in the post", value=self.indexs,values=self.tags,scroll_exit=True)

        #self.f2 = self.add(npyscreen.TitleText, name="Status")
        self.status_list=sorted(get_status_list())
        self.b = self.add(npyscreen.TitleSelectOne, name="Status",value=[],values=self.status_list)

    def on_ok(self):
        tags = [self.a.get_values()[x] for x in self.a.get_value()]
        update_tags_from_post(self.post,tags)
        #tag_result["0"]=self.post
        #tag_result["1"]=[self.a.get_values()[x] for x in tags]

        selected = self.b.get_value()[0]
        #tag_result["0"]=self.status_list[selected]
        update_status_from_post_name(self.post,self.status_list[selected])

        #self.parentApp.switchForm(None)
        self.parentApp.switchFormPrevious()
    def on_cancel(self):
            self.parentApp.switchFormPrevious()

    def setup(self,post):
        self.tags = list(get_tags())
        self.post = post

        self.selected = get_tags_from_post_name(post)[0][0]
        self.selected = self.selected.split("/")[:-1]
        
        self.indexs = []

        for i,tag in enumerate(self.tags):
            if tag in self.selected:
                self.indexs.append(i)

        print(self.indexs)
        self.result="Failure"






class Select_post(npyscreen.NPSApp):

    @cursor
    def get_posts(self,**kwargs):
        result = kwargs["con"].execute("""
                select name from posts 
                where status not like "trash"
                order by name asc;
                """)
        return [x[0] for x in list(result)]

    #@cursor
    #def get_trash(self,**kwargs):
    #    result = kwargs["con"].execute("""
    #            select name from posts 
    #            where status like "trash"
    #            order by name asc;
    #            """)
    #    result = [prepare_string(x[0]) for x in list(result)]
    #    return "~".join(result)

    def main(self):

        cap = lambda x:x[0].upper()+x[1:]

        values = self.get_posts()
        #values = sorted(values)

        F = npyscreen.Form(name="Name of the post which you want to delete",)
        #fn = F.add(npyscreen.TitleText, name="",
        #    max_height=3)
        t = F.add(npyscreen.TitleSelectOne, max_height=len(values), name="Category",value=[0,],
                values=[prepare_string(v.replace("_"," ")) for v in values],scroll_exit=True)
        
        F.edit()

        self.result={"name":values[t.get_value()[0]]}
        #self.result=self.values

    

if __name__ == "__main__":
    App=TestApp()
    App.run()
