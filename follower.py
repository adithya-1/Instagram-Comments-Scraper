from selenium import webdriver
import pandas as pd
import time

df = pd.read_excel('comments.xlsx')
names = df['name']

followers = []
following = []
for i in range(0, len(names)):
    driver = webdriver.Chrome(
        'D:\My apps\Instagram-Comments-Scraper\.venv\Scripts\chromedriver.exe')
    url = 'https://www.instagram.com/'+names[i]+'/'
    driver.get(url)
    time.sleep(3)
    try:
        close_button = driver.find_element_by_class_name('xqRnw')
        close_button.click()
    except:
        pass
    followers.append(driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').text)
    following.append(driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').text)
    print(followers)
    print(following)
    driver.close()
df['Followers'] = followers
df['Following'] = following
df.to_excel('comments.xlsx')
