import sqlite3
from createShared import createSharedBook
from flask import g
import os
import hashlib
import sys
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.userstore.constants as UserStoreConstants
from evernote.edam.error.ttypes import EDAMUserException
from evernote.edam.error.ttypes import EDAMSystemException
from evernote.edam.error.ttypes import EDAMNotFoundException
from evernote.edam.error.ttypes import EDAMErrorCode
"""

def get_db():
    db = getattr(g, '/tmp/flaskr.db', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
"""
dev_token = "put your dev token here"
client = EvernoteClient(token='S=s1:U=8f602:E=14fa474b498:C=1484cc384b8:P=1cd:A=en-devtoken:V=2:H=c895959cccfaa98b58c5b3fc85942b2f')
userStore = client.get_user_store()
s='S=s1:U=8f602:E=14fa474b498:C=1484cc384b8:P=1cd:A=en-devtoken:V=2:H=c895959cccfaa98b58c5b3fc85942b2f'
user = userStore.getUser()
#print user
noteStore = client.get_note_store()
shbook=createSharedBook()
noteStore.createSharedNotebook(s, shbook)
print shbook
