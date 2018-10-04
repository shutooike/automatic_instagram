# user INFO
username = ""
password = ""

# hashtag INFO
hashtagList = ["","",""]

# linenotify token INFO
line_notify_token = ''

# import
import datetime
import schedule
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# url INFO
instagramURL = "https://www.instagram.com"
loginURL = "https://www.instagram.com/accounts/login/"
profileURL = "https://www.instagram.com/{}/".format(username)

# defining xpaths and selectors
likeXpath = '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span'
searchXpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
numberOfFollowersXpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'
nextPageSelector = 'a.coreSpriteRightPaginationArrow'
postSelector = 'div._9AhH0'
buttonXpath = '/html/body/div[3]/div/div/div/div[3]/button[1]'

# post list
postlist = []

# job
job = 0

# total likes
totalLikes = 0

# defining linenotify
def linenotify(message):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)

while job < 5:
    # starting a new browser session
    browser = webdriver.Chrome()

    # login
    browser.get(loginURL)
    browser.find_element_by_name("username").send_keys(username)
    browser.find_element_by_name("password").send_keys(password,Keys.RETURN)

    # push button
    sleep(3)
    browser.implicitly_wait(10)
    browser.find_element_by_xpath(buttonXpath).click()

    # getting number of followers
    sleep(3)
    browser.get(profileURL)
    followers = browser.find_element_by_xpath(numberOfFollowersXpath)
    dt_now = datetime.datetime.now()
    followersReport = "You have {} followers at {}".format(followers.text,dt_now)
    message = '{}'.format(followersReport)
    linenotify(message)

    # hashtag loop
    for hashtagName in hashtagList:
        sleep(3)
        browser.get(instagramURL)
        sleep(3)

    # searching for the hashtag
        browser.implicitly_wait(10)
        browser.find_element_by_xpath(searchXpath).send_keys("#{}".format(hashtagName))
        sleep(5)
        browser.find_element_by_xpath(searchXpath).send_keys(Keys.RETURN,Keys.RETURN)

    # making a postList
        sleep(5)
        browser.implicitly_wait(10)
        postList = browser.find_elements_by_css_selector(postSelector)

    # automatic like
        for post in postList:
            sleep(3)
            post.click()
            nextCounter = 0
            likedCounter = 0

            while nextCounter < 9:
                sleep(2)
                browser.implicitly_wait(10)
                browser.find_element_by_css_selector(nextPageSelector).click()
                nextCounter += 1

            while likedCounter < 1:
                try:
                    sleep(3)
                    browser.implicitly_wait(10)
                    browser.find_element_by_xpath(likeXpath).click()
                    browser.implicitly_wait(10)
                    likedCounter += 1
                    browser.find_element_by_css_selector(nextPageSelector).click()
                except:
                    break

            break

        totalLikes += likedCounter
        interimReportList = ["\n"]
        interimReportList.append("liked {} posts of #{}\n".format(likedCounter,hashtagName))
        continue

    # report
    finalReport = "\nliked {} posts".format(totalLikes)
    interimReport = "".join(interimReportList)
    message = '{}'.format(interimReport + finalReport)
    linenotify(message)
    sleep(3)

    # clean exit
    browser.close()
    misson += 1
    sleep(1800)
