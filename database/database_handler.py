'''
    This module handles all the operations related to
    database needed by server_operator.
'''
from os import system
import sqlite3


def retrieve_clients():
    '''
        This function retrieves client host credencials
        and returns in correct formate.
    '''
    conn = sqlite3.connect("/home/knife/MyPlaxonicWork/youtube-viewer/server.db")
    cur = conn.cursor()
    data = cur.execute("SELECT ip, user, pass from client")
    datalist = []
    for row in data:
        datalist.append([row[1],row[0],row[2]])
    conn.close()
    return datalist

def retrieve_tasks():
    '''
        This function retrieves client host credencials
        and returns in correct formate.
    '''
    conn = sqlite3.connect("/home/knife/MyPlaxonicWork/youtube-viewer/server.db")
    cur = conn.cursor()
    data = cur.execute("SELECT videourl, numberofviews from pendingtask")
    datalist = []
    for row in data:
        datalist.append([row[0],int(row[1])])
    conn.close()
    return datalist

def add_task_from_local_to_database():
    system("tmux new -d -s taskadder")
    system("tmux send-keys 'python3 task_adder_from_local_to_database.py' ENTER")
add_task_from_local_to_database()