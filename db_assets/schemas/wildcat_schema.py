import sqlite3

conn = sqlite3.connect('wildcats.db')
c = conn.cursor()

c.execute("""CREATE TABLE cats (
		name blob,
		image_path blob,
		description blob
		)""")

conn.commit()
conn.close()