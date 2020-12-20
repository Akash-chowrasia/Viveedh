'''
    This Module is the key module which performs the key operations
    and desision making processes of server.
'''
from os import system
import csv

def data_collector():
    '''
        This function asks the server operator for URL
        and Number of views needed.
    '''
    video_url = input("Enter URL : ")
    views = int(input("Enter Number Of Views : "))
    return [video_url, views]

def host_finder():
    '''
        This function reads the host_list and returns into
        a list variable.
    '''
    temp = []
    with open("host_list.csv") as file:
        thereader = csv.reader(file)
        for row in thereader:
            print(row)
            temp.append([f'{row[0]}', f'{row[1]}', f'{row[2]}'])
    return temp

def views_parser(total_views,number_of_host):
    '''
        This function desides how many hosts are needed and
        how many views are needed to be completed by each host.
    '''
    if 2*number_of_host < total_views:
        return [(total_views//number_of_host),number_of_host]
    return [(total_views//2), (number_of_host//(2*total_views))]

def start_host_process(key_data):
    '''
        This function creates new tmux session for each host and
        executes host_operator program for each host.
    '''
    for i in range(key_data[2]):
        system("tmux new -d -s host%i"%i)
        system("tmux send-keys 'python3 host_operator.py %s %d %s %s %s' ENTER"\
            %(key_data[0],key_data[1],key_data[3][i][0],key_data[3][i][1],key_data[3][i][2]))

# Driver code
if __name__ == "__main__":
    data = data_collector()
    host = host_finder()
    views_and_host_required = views_parser(data[1],len(host))
    start_host_process([data[0],views_and_host_required[0],views_and_host_required[1],host])
