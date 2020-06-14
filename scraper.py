import excel_exporter
from selenium import webdriver
import time
import sys

driver = webdriver.Chrome(
    'D:\My apps\Instagram-Comments-Scraper\.venv\Scripts\chromedriver.exe')
driver.get(sys.argv[1])
time.sleep(3)

# if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass


try:
    load_more_comment = driver.find_element_by_css_selector(
        '.MGdpg > button:nth-child(1)')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed() and i < int(10):
        load_more_comment.click()
        time.sleep(1.5)
        load_more_comment = driver.find_element_by_css_selector(
            '.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass

user_names = []
user_comments = []
user_likes = []
user_replies = []

comment = driver.find_elements_by_class_name('Mr508')

for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()

    try:
        likes = container.find_element_by_tag_name('button').text
        if likes == 'Reply':
            likes = 0
        try:
            likes = likes.replace('likes', '')
        except:
            pass
        try:
            likes = likes.replace('like', '')
        except:
            pass
    except:
        likes = 0
    try:
        replies = c.find_element_by_class_name('EizgU').text
        replies = replies.replace('View replies', '')
    except:
        replies = 0
    user_likes.append(likes)
    user_names.append(name)
    user_comments.append(content)
    user_replies.append(replies)


user_names.pop(0)
user_comments.pop(0)
user_likes.pop(0)
user_replies.pop(0)


excel_exporter.export(user_names, user_comments, user_likes,
                      user_replies)

driver.close()
