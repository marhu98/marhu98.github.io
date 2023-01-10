"""
Corrects time stamps on post database by inserting them
slowly.
Respects the order they already had.
"""

import sqlite3
from time import sleep

con = sqlite3.connect('db/web.sqlite3')
cur = con.cursor()

row = list(cur.execute('select * from posts'))

cur.execute("""
CREATE TABLE IF NOT EXISTS "posts_"(id integer primary key autoincrement, category text,name text unique, status text check (status in ("draft","publish","trash","wip","updating")), tags text default "",date datetime default current_timestamp);
""")
for el in row:
    cur.execute("""
    insert into  posts_(category,name,status,tags)
    values (?,?,?,?)
    """,el[1:-1])
    print(f"Inserting: {el[2]}")
    sleep(1)
cur.execute("""
drop table "posts"
""")
cur.execute("""
alter table "posts_" rename to "posts"
""")

con.commit()
con.close()
