import sqlite3

#if you want to add more cats, add to this list, use the same format. Note how to last {} doesn't have a comma after it
cats = [
    {
        "name": "Travis",
        "path": "../static/images/travis.jpg",
        "description": "Filler text is text that shares some characteristics of a real written text, but is random or otherwise generated. It may be used to display a sample of fonts, generate text for testing, or to spoof an e-mail spam filter."
    },
    {
        "name": "Hale",
        "path": "../static/images/hale.jpg",
        "description": "Filler text is text that shares some characteristics of a real written text, but is random or otherwise generated. It may be used to display a sample of fonts, generate text for testing, or to spoof an e-mail spam filter."
    },
    {
        "name": "Abhinav",
        "path": "../static/images/abhinav.jpg",
        "description": "Filler text is text that shares some characteristics of a real written text, but is random or otherwise generated. It may be used to display a sample of fonts, generate text for testing, or to spoof an e-mail spam filter."
    }
]

#inserting into the cats table in the wildcats database
conn = sqlite3.connect('wildcats.db')
c = conn.cursor()

for i in cats:
    c.execute("""INSERT INTO cats VALUES (?, ?, ?)""", (i.get("name"), i.get("path"), i.get("description")))
    conn.commit()

conn.close()