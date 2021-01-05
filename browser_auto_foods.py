# browser_auto_foods.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome("./driver/chromedriver")

location = input("検索対象入力：")
favorite_foods = ["七隈", "天神", "中洲", "博多", "藤崎"]

for i, food in enumerate(favorite_foods):
    if i > 0:
        # 新しいタブ
        chrome.execute_script("window.open('','_blank');")
        chrome.switch_to.window(chrome.window_handles[i])

    # グーグルを開く
    chrome.get("https://www.google.co.jp")

    # 検索ワード入力
    search_box = chrome.find_element_by_name("q")
    search_words = location, food
    search_box.send_keys(" ".join(search_words))

    # 検索実行
    search_box.send_keys(Keys.RETURN)
    print(chrome.title)
    print(enumerate(favorite_foods))

# 先頭のタブに戻る
chrome.switch_to.window(chrome.window_handles[0])
