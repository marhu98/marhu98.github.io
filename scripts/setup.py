from setuptools import setup

setup(
    name="blog",
    version="0.0.2",
    py_modules=['blog'],
    install_modules=['Click',"npyscreen","sqlite3"],
    entry_points={
        'console_scripts':['blog=main:main']
        }
)
