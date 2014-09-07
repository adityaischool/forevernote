import sqlite3
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


def createSharedBook():
	sharedNotebook = Types.SharedNotebook()
	sharedNotebook.notebookGuid = notebook.guid
	sharedNotebook.allowPreview = True
	sharedNotebook.privilege = Types.SharedNotebookPrivilegeLevel.MODIFY_NOTEBOOK_PLUS_ACTIVITY
	sharedNotebook.email = "aditya86254@gmail.com"
	return sharedNotebook