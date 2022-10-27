import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


PATH = r"C:\Users\roige\source\repos\TwitterInfluencersFinder\TwitterInfluencersFinder\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def login():
    driver.get("https://mobile.twitter.com/home")
    print (driver.title)
    
    time.sleep(3)
    user = driver.find_element_by_name("text")
    time.sleep(1)
    user.send_keys("hakatav_hatsvai")
    time.sleep(1)
    user.send_keys(Keys.RETURN)
    time.sleep(1)
    password = driver.find_element_by_name("password")
    time.sleep(1)
    password.send_keys("Myxbox360")
    time.sleep(1)
    password.send_keys(Keys.RETURN)
    time.sleep(1)

 
def reply(link):

    driver.get(link)

    time.sleep(3)
    driver.find_element_by_css_selector(
                        '.css-18t94o4[data-testid ="reply"]'
                    ).click()
    time.sleep(1)
    pg.typewrite("https://t.me/hakatav")
    time.sleep(1)
    pg.hotkey('ctrl', 'enter')
    time.sleep(3)

def findTweets(link):
    driver.get(link)
    time.sleep(3)
    pg.scroll(-20200)
    time.sleep(3)
    pg.click(x=365, y=962)
    return driver.current_url



def get_names_from_File():
    with open("names1 - Copy.txt", 'r') as read_obj:
        t3k = read_obj.readlines()
    return t3k

def cor_names(names):
    correct_names = []
    for name in names:
        correct_names.append(name[:-1])
    return correct_names

def main():
    login()
    names = get_names_from_File()
    names = cor_names(names)
    fails = 0
    for name in names:
        try:
            Myurl = findTweets('https://mobile.twitter.com/'+name)
        except:
            fails+=1
            pass
        try:
            fails = 0
            reply(Myurl)
        except:
            fails+=1
            pass
        if fails == 5:
            time.sleep(600)
        print(name)
    
main()


