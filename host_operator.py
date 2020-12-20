'''
    This Module is the main door to get connected with the
    client host. this module is bieng executed differently
    by Server operator for each session to get connected with
    each client host on different sessions.

    **ARGUMENT DESCRIPTION**

    URL : argv[1]
    Number of views : argv[2]
    Host User : argv[3]
    Host IP : argv[4]
    Host Pass : argv[5]
'''
from os import system
from sys import argv

def sshwork():
    '''
        This function logins to the client host's user with given
        credencials and executes window operator over there into
        respective session.
    '''
    system("sshpass -p %s ssh -X %s@%s 'python3 window_operator.py %s %s %s'"\
        %(argv[5],argv[3],argv[4],argv[1],argv[2],argv[3]))

# Driver code
if __name__ == "__main__":
    sshwork()
