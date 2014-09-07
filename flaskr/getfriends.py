import sqlite3
from flask import g
"""
def get_db():
    db = getattr(g, '/tmp/flaskr.db', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

def getBuds(myname):
	db = getattr(g, '/tmp/flaskr.db', None)
	query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc')
	cur = g.db.execute(query)
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

    """
def getBuds(myname):
	conn = sqlite3.connect('/tmp/flaskr.db')
	c = conn.cursor()
	query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	c.execute(query)
	results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	conn.close()
	return results

if __name__ == '__main__':
	d= getBuds('aditya')
	for e in d:
		print e['fname']