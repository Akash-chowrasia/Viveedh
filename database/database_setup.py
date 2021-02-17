'''
    This mudule setups a new sqlite3 database if database
    does not exists.
'''
import sqlite3

def create_client_table():
    '''
        This function creates client table into
        the database.
    '''
    conn.execute('''CREATE TABLE client
            (ip TEXT PRIMARY KEY NOT NULL,
            user TEXT NOT NULL,
            pass TEXT);''')

def create_pending_task_table():
    '''
        This function creates pendingtask table
        into the database.
    '''
    conn.execute('''CREATE TABLE pendingtask
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            videourl TEXT NOT NULL,
            numberofviews CHAR(7) NOT NULL,
            videolength CHAR(4));''')

def create_completed_task_table():
    '''
        This function creates completedtask table
        into the database.
    '''
    conn.execute('''CREATE TABLE completedtask
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            videourl TEXT NOT NULL,
            numberofviews CHAR(7) NOT NULL,
            videolength CHAR(4));''')

# Driver code
if __name__ == "__main__":
    conn = sqlite3.connect("/home/knife/MyPlaxonicWork/youtube-viewer/server.db")
    create_client_table()
    create_pending_task_table()
    create_completed_task_table()
    conn.commit()
    conn.close()
