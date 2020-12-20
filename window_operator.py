'''
    This Module is to be executed at client host.
    This Module decides the number of windows
    to be opened on the client host and how many
    views are needed to be completed by each host.
    After, finding these two stuffs it creates
    desired number of windows in different tmux
    sessions and executes viewer over each window.

    **ARGUMENT DESCRIPTION**

    URL : argv[1]
    Number Of Views : argv[2]
    Host User : argv[3]
'''
from sys import argv
from os import system

def views_parser(total_views):
    '''
        This function finds the number of windows
        to be opened and how many views needed to
        be completed by each window.
    '''
    if total_views<=10:
        return [total_views,1]
    if total_views > 40:
        return [total_views//5,5]
    return [total_views//3,3]


def start_window_process(data):
    '''
        This function creates desired number of tmux
        sessions and executes viewer over each session
        with the target number of views and URL.
    '''
    for i in range(data[2]):
        system("tmux new -d -s window%s-%d"%(argv[3],i))
        system("tmux send-keys 'python3 a.py %s %d' ENTER"%(data[0],data[1]))

# Driver code
if __name__ == "__main__":
    views_and_window_required = views_parser(int(argv[2]))
    start_window_process([argv[1],views_and_window_required[0],views_and_window_required[1]])
