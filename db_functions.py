import sqlite3
import sys

def get_cats():
    conn = sqlite3.connect("wildcats.db")
    c = conn.cursor()

    c.execute("""SELECT * FROM cats""")
    cats = c.fetchall()

    return cats

def search(query_string):
    tokenized_string = query_string.split()

    conn = sqlite3.connect("wildcats.db")
    c = conn.cursor()

    initial_search = []

    for i in tokenized_string:
        query = f"%{i}%"
        
        c.execute(f"""SELECT * FROM cats WHERE name LIKE (?)""", (query,))
        x = c.fetchall()
        initial_search.append(x)

        c.execute(f"""SELECT * FROM cats WHERE description LIKE (?)""", (query,))
        x = c.fetchall()
        initial_search.append(x)

    #print(f"initial_search: {initial_search}", file=sys.stderr)

    final_search = []
		
    exists = False
    for k in initial_search:
        for i in k:
            for j in final_search:
                if i[1] == j[1]:
                    exists = True
            if exists != True:
                final_search.append(i)
            exists = False

    return final_search

        