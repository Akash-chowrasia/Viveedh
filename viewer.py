'''
    This Module is to be executed over client host.
    this module scraps the target youtube video and
    plays it successfully to accomplish the task.

    PYLINT TEST Rating = 9.21/10.
'''
from os import system
from time import sleep
from random import randint
from sys import argv
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

def url_decoder(url):
    '''
        This function decodes the encoded string passed
        by the server and returns to the driver code.
    '''
    url_list = url.split('+')
    decoded_url = ''
    for char in url_list:
        decoded_url += chr(int(char))
    return decoded_url

def max_time_finder():
    '''
        This function finds the length of the video
        in seconds.
    '''
    max_time_element = viewer.find_element_by_xpath("//div[@id='movie_player']/\
        descendant::div[@role='slider']")
    return int(max_time_element.get_attribute("aria-valuemax"))

def mute_sound():
    '''
        This function click's the mute button to make system
        sound resistent by scraping the element.
    '''
    viewer.find_element_by_xpath("//div[@id='movie_player']/\
        descendant::button[@title='Mute (m)']").click()
def play_video():
    '''
        This function click's over play button to play video
        by scraping the element.
    '''
    viewer.find_element_by_xpath("//div[@id='movie_player']/\
        descendant::button[contains(@title, 'Play')]").click()

def ad_finder():
    '''
        this function checks if ad is running or not.
    '''
    viewer.find_element_by_xpath("//*[contains(@id, 'simple-ad-badge')]")

# Driver code
if __name__ == "__main__":
    while True:
        try:
            opt = Options()
            opt.headless = True
            viewer = webdriver.Firefox(options=opt)
            viewer.get(url_decoder(argv[1]))
            mute_sound()
            play_video()
            break
        except:
            try:
                viewer.quit()
                continue
            except:
                pass
    COUNTER = 0
    while COUNTER<=int(argv[2]):
    #while True:
        while True:
            try:
                ad_finder()
            except:
                print("Ad completed...")
                sleep(10)
                break
        max_time = max_time_finder()
        try:
            play_video()
            print("video was paused")
        except:
            pass
        try:
            sleep(randint(160,min(600,max_time-50)))
        except:
            print("Ad found...")
            continue
        while True:
            try:
                viewer.refresh()
                break
            except:
                continue
        COUNTER += 1
    viewer.quit()
    system("exit")
