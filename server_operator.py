'''
    This Module is the key module which performs the key operations
    and desision making processes of server.
'''
from os import system
import subprocess
#import csv
from database.database_handler import *

def url_encode(strng):
    '''
        This function incodes the url into the formate
        of unicode code charecter.
    '''
    new_string = str(ord(strng[0]))
    for char in strng[1::]:
        new_string += '+'
        new_string += str(ord(char))
    return new_string

def active_host_finder(host_list):
    """
    This function returns the list of active client.
    it uses the concept of PING command to achive the target.
    """
    active_host = []
    for host_data in host_list:
        command = ['ping', '-c', '1', host_data[1]]
        if subprocess.call(command) == 0:
            active_host.append(host_data)
    return active_host

def data_collector():
    '''
        This function asks the server operator for URL
        and Number of views needed.
    '''
    #return [video_url, views]
    return retrieve_tasks()[0]

def host_finder():
    '''
        This function reads the host_list and returns active
        hosts into a list variable.
    '''
    '''temp = []
    with open("host_list.csv") as file:
        thereader = csv.reader(file)
        for row in thereader:
            print(row)
            temp.append([f'{row[0]}', f'{row[1]}', f'{row[2]}'])
    return active_host_finder(temp)'''
    return active_host_finder(retrieve_clients())


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
        encoded = url_encode(key_data[0])
        system("tmux new -d -s host%i"%i)
        system("tmux send-keys 'python3 host_operator.py %s %d %s %s %s' ENTER"\
            %(encoded,key_data[1],key_data[3][i][0],key_data[3][i][1],key_data[3][i][2]))

# Driver code
if __name__ == "__main__":
    data = data_collector()
    host = host_finder()
    views_and_host_required = views_parser(data[1],len(host))
    start_host_process([data[0],views_and_host_required[0],views_and_host_required[1],host])
