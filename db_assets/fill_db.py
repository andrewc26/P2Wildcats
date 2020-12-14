import sqlite3

#if you want to add more cats, add to this list, use the same format. Note how to last {} doesn't have a comma after it
cats = [
    {
        "name": "Wildcat Picture 1",
        "path": "../static/images/travis.jpg",
        "description": "Here we will write a paragraph about the specific animal and a short description with some information"
    },
    {
        "name": "Wildcat Picture 2",
        "path": "../static/images/hale.jpg",
        "description": "Here we will write a paragraph about the specific animal and a short description with some information"
    },
    {
        "name": "Wildcat Picture 3",
        "path": "../static/images/abhinav.jpg",
        "description":"Here we will write a paragraph about the specific animal and a short description with some information"
    }
]

#inserting into the cats table in the wildcats database
conn = sqlite3.connect('wildcats.db')
c = conn.cursor()

for i in cats:
    c.execute("""INSERT INTO cats VALUES (?, ?, ?)""", (i.get("name"), i.get("path"), i.get("description")))
    conn.commit()

conn.close()