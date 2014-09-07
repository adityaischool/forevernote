import sqlite3

conn = sqlite3.connect('/tmp/flaskr.db')
c = conn.cursor()
c.execute("INSERT INTO friends VALUES ('aditya','alex','thenote')")
c.execute("INSERT INTO friends VALUES ('aditya','friend2','thenote')")
c.execute("INSERT INTO friends VALUES ('aditya','friend3','thenote')")
c.execute("INSERT INTO friends VALUES ('aditya','friend4','thenote')")
c.execute("INSERT INTO friends VALUES ('aditya','friend5','thenote')")

conn.commit()

#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc')
#cur = g.db.execute(query)
#entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
#return render_template('show_entries.html', entries=entries)