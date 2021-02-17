'''
    This module is helper for database handler's task.
'''

from selenium.webdriver.firefox.options import Options
from selenium import webdriver

def max_time_finder(url_link):
    '''
        This function finds the length of the video
        in seconds.
    '''
    print("calculating video length, please wait....")
    while True:
        try:
            opt = Options()
            opt.headless = True
            length_finder = webdriver.Firefox(options=opt)
            length_finder.get(url_link)
            max_time_element = length_finder.find_element_by_xpath("//div[@id='movie_player']/\
                descendant::div[@role='slider']")
            while True:
                try:
                    max_time =  int(max_time_element.get_attribute("aria-valuemax"))
                    if max_time >= 240:
                        break
                    raise ValueError("add found")
                except:
                    continue
            length_finder.quit()
            print("Video length calculated...")
            return str(max_time)
        except:
            continue
