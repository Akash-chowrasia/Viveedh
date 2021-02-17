'''
    This Module setups all the dependency over client
    host to make it compatible for the system.
'''
from os import system

def update_system():
    '''
        This function updates system with using
        apt package.
    '''
    system("sudo apt-get update")

def install_driver():
    '''
        This function install's drivers into client host
        like geckodriver and chromedriver and setups them
        into correct position "/usr/local/bin"
    '''
    system("sudo chmod 777 driver_installer.sh")
    system("./driver_installer.sh")
    update_system()

def install_tmux():
    '''
        This function install's tmux over client host
        using which system creates sessions to open new
        windows.
    '''
    system("sudo apt-get install tmux")

def install_selenium():
    '''
        This function install's pip inataller and selenium
        packeg into the client host for executing the viiewer.
    '''
    system("sudo apt-get install python3-pip")
    system("pip3 install selenium")

# Driver code
if __name__ == "__main__":
    update_system()
    install_driver()
    install_tmux()
    install_selenium()
