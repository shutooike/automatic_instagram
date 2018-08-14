# user INFO
username = ""
password = ""

# hashtag INFO
hashtagList = ["","",""]

# import
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# url hashtag INFO
instagramURL = "https://www.instagram.com"
loginURL = "https://www.instagram.com/accounts/login/"

# define xpaths and selectors
likeXpath = '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span' #いいねボタン
searchXpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input' #検索
nextPageSelector = 'a.coreSpriteRightPaginationArrow' #次へボタン
postSelector = 'div._9AhH0' #投稿の画像部分のselector

# post list
postlist = []

# total likes
totalLikes = 0

# starting a new browser session
browser = webdriver.Chrome()

# navigating to Instagram
browser.get(instagramURL)

# login
browser.get(loginURL)
browser.find_element_by_name("username").send_keys(username)
browser.find_element_by_name("password").send_keys(password,Keys.RETURN)

# hashtag loop
for hashtagName in hashtagList:
    sleep(3)
    browser.get(instagramURL)

# searching for the hashtag
    browser.implicitly_wait(10)
    browser.find_element_by_xpath(searchXpath).send_keys("#{}".format(hashtagName))
    sleep(3)
    browser.find_element_by_xpath(searchXpath).send_keys(Keys.RETURN,Keys.RETURN)

# making a postList
    sleep(3)
    postList = browser.find_elements_by_css_selector(postSelector)

# automatic like
    for post in postList:
        post.click()
        nextCounter = 0
        likedCounter = 0

        while nextCounter < 9: 
            sleep(2)
            browser.implicitly_wait(10)
            browser.find_element_by_css_selector(nextPageSelector).click()
            nextCounter += 1

        while likedCounter < 50:
            try:
                sleep(2)
                browser.find_element_by_xpath(likeXpath).click()
                browser.implicitly_wait(10)
                likedCounter += 1
                browser.find_element_by_css_selector(nextPageSelector).click()
            except:
                break

        break

    totalLikes += likedCounter
    print("liked {0} posts of #{1}".format(likedCounter,hashtagName))
    continue

print("liked {} posts".format(totalLikes))
sleep(3)

# clean exit
browser.close()
