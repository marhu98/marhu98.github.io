# This is my webpage

The idea for this project is to make a website generating template.
So you give some toml with some basic instructions and it generates a website template

Create new posts in the website using the lb tool.

Write markdown with php code in it: lb will automatically compile it to html using a pandoc template than handles
everything: css, nav bar, routing, etc...


#Make your ownn website:

You can make your own website from this code, it is very simple:
Start a new website with:
`make init`
If you want to update the website after editing a file:
`make compile`
Or if you changed the template file: default.php:
`make all`

You can automate this process if you have entr installed (which is highly recomended):
```
ls static/*md | entr -c 'make compile'
```

If you decide to add a new file you can correct the database running:
`make fix`

Not enough options: Make your own and make a pull request!
All contribution is very welcome.


#Use the light blog tool:
You can manage your website by using the lb tool. To know all the options,
just run:
```
lb --help
```
Make sure you run make install first to install lb.
