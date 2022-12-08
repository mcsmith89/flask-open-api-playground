from datetime import datetime
from flask import abort
import sqlite3

#SQLite connection
def queryDB(query, type):
    if type == "post":
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            queryResult = cursor.execute(query)
            connection.commit()
            connection.close()
        except:
            print(f"Error {query}")
    if type == "get":
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            return(cursor.execute(query))
        except:
            print(f"Error {query}")
    

#Get methods/endpoint functions
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    players = {}
    queryAllPLayers = f"SELECT * FROM players;"
    for player in queryDB(queryAllPLayers, "get").fetchall():
        players.update({player[1]:{"fname":player[0], "lname":player[1], "created":player[2]}})
    return(list(players.values()))


#FIX THIS HERE 
def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")
    createPlayer = f'''
        INSERT INTO players (fname, lname, created)
        VALUES
        ("{lname}", "{fname}", DATE("now"));
    '''
    try:
        queryDB(createPlayer, "post")
        return(200)
    except:
        abort(
            406,
            f"Issue adding {fname} {lname}"
        )
    
#Left off on Create a New Person