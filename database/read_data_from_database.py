'''
    This modules reads database as per requirement
    created to be used by server operator from console.
'''
import sqlite3

def read_client():
    '''
        This function reads all the data of client table and
        prints into console.
    '''
    data = cur.execute("SELECT ip, user, pass from client")
    count = 1
    for row in data:
        print(count,") **************************")
        print(list(row))
        print("IP : ",row[0])
        print("USER : ",row[1])
        print("PASSWORD : ",row[2])
        count += 1

def read_pending_task():
    '''
        This function reads all the data of client table and
        prints into console.
    '''
    data = cur.execute("SELECT id, videourl, numberofviews, videolength from pendingtask")
    count = 1
    for row in data:
        print(count,") **************************")
        print("ID : ",row[0])
        print("VIDEO URL : ",row[1])
        print("NUMBER OF VIEWS : ",row[2])
        print("VIDEO LENGTH : ",row[3])
        count += 1

# Driver code
if __name__ == "__main__":
    conn = sqlite3.connect("/home/knife/MyPlaxonicWork/youtube-viewer/server.db")
    cur = conn.cursor()
    print("1) Enter 1 to Read Client Data..\n2) Enter 2 to Read pending Tast Data...")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        read_client()
    else:
        read_pending_task()
    conn.close()
