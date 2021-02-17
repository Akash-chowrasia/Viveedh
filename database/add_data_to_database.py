'''
    This module adds data to databse by asking to
    the server operator from console.
'''
import sqlite3
import csv

def add_client():
    '''
        This function add's new host data to
        client's table.
    '''
    number_of_clients = int(input("Number of clients you want to enter: "))
    for i in range(1,number_of_clients+1):
        print("***** Data for Client %d *****"%i)
        ipadress = input("IP:")
        user = input("Username:")
        password = input("Password:")
        cur.execute("INSERT INTO client (ip,user,pass) \
        VALUES (?,?,?)",(ipadress, user, password))
        conn.commit()

def add_task(cur):
    '''
        This function add's new host data to
        client's table.
    '''
    number_of_task = int(input("Number of tasks you want to enter: "))
    for i in range(1,number_of_task+1):
        print("***** Data for Task %d *****"%i)
        videourl = input("URL:")
        numberofviews = input("Number of views:")
        cur.writerow([videourl,numberofviews])

# Driver code
if __name__ == "__main__":
    print("1) Enter 1 to ADD a HOST:\n2) Enter 2 to ADD a TASK:")
    choice = int(input("Enter choice:"))
    if choice==1:
        conn = sqlite3.connect("/home/knife/MyPlaxonicWork/youtube-viewer/server.db")
        cur = conn.cursor()
        add_client()
        conn.close()
    else:
        with open("local_task.csv",'a',newline='') as obj:
            cur = csv.writer(obj)
            add_task(cur)
