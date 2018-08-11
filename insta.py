#--------------- 以下 script ---------------#

# user INFO
username = ""
password = ""

# hashtag INFO
hashTagName = ""

# import
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# url hashtag INFO
instagramURL = "https://www.instagram.com" #インスタグラム
loginURL = "https://www.instagram.com/accounts/login/" #ログイン

# define a xpath and a selector
likeXpath = '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span' #いいねボタン
searchXpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input' #検索
nextPageSelector = 'a.coreSpriteRightPaginationArrow' #次へボタン
postSelector = 'div._9AhH0' #投稿の画像部分のselector

# list
postlist = []

# counter
likedCounter = 0

# starting a new browser session
browser = webdriver.Chrome()

# navigating to Instagram
browser.get(instagramURL)

# login
browser.get(loginURL)
browser.find_element_by_name('username').send_keys(username)
browser.find_element_by_name('password').send_keys(password,Keys.RETURN)

# navigating to hashtag webpage
browser.implicitly_wait(10)
browser.find_element_by_xpath(searchXpath).send_keys("#{}".format(hashTagName))
sleep(3)
browser.find_element_by_xpath(searchXpath).send_keys(Keys.RETURN,Keys.RETURN)

# make a postList
sleep(3)
postList = browser.find_elements_by_css_selector(postSelector)

# automatic like
for post in postList:
    post.click()

    while True:
        try:
            sleep(2)
            browser.find_element_by_xpath(likeXpath).click()
            browser.implicitly_wait(10)
            likedCounter += 1
            browser.find_element_by_css_selector(nextPageSelector).click()
        except:
            break
    break


print("You liked {} media".format(likedCounter))
sleep(3)

# clean exit
browser.close()
