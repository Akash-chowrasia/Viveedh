'''
    This module adds all the tasks from
    csv file to database by calculating
    there video duration.
'''
import sqlite3
import os
import csv
from task_manager.database_task_manager import max_time_finder

#Driver code
if __name__ == "__main__":
    conn = sqlite3.connect("/home/knife/MyPlaxonicWork/youtube-viewer/server.db")
    cur = conn.cursor()
    with open("local_task.csv") as obj:
        file_cur = csv.reader(obj)
        for row in file_cur:
            print(f'{row[0]}')
            print(f'{row[1]}')
            videourl = f'{row[0]}'
            numberofviews = f'{row[1]}'
            videolength = max_time_finder(videourl)
            cur.execute("INSERT INTO pendingtask (videourl,numberofviews,videolength) \
            VALUES (?,?,?)",(videourl,numberofviews,videolength))
            conn.commit()
            '''with open("temp.csv",'a',newline='') as write_obj:
                write_cur = csv.writer(write_obj)
                write_obj.writerow(row)'''
    os.remove("local_task.csv")
    cur.close()