# pip install some libraries, like selenium, bs4 and plyer in CMD terminal
# import from libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from plyer import notification
import os

# Website you would like to track price. ***ATTENTION*** it won't work with books, comics and magazines
amazon_page = "https://www.amazon.com/PlayStation-PS5-Console-Ragnarök-Bundle-5/dp/B0BHC395WW/ref=lp_16225016011_1_1"

#Before executing, make sure to download at https://chromedriver.chromium.org/downloads the most recent version of your Google Chrome browser.
#Acesssing the given website in a new windown of Google Chrome
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome()

driver.get(amazon_page)
driver.implicitly_wait(100)

#Setting the Amazon page to scrap into Beautiful Soup
page = driver.page_source

soup = BeautifulSoup(page, "html.parser")

##Finding the price and name of the product
price = (soup.find("span", {"class" : "a-offscreen"})).text
product_name = (soup.find("span", {"class" : "a-size-large product-title-word-break"})).text
clean_product_name = (product_name.replace("        ",""))
clean_product_name2 = (clean_product_name.replace("      ",""))

#Creating a function to in order to pop-up notification.
def notification_on(title_my, message_my):
    notification.notify(title = title_my, message = message_my, app_icon = None, timeout = 10)

message = f" The price checked for {clean_product_name2}currently is {price}"
notification_on("Amazon Price Tracking", message)

#Enjoy :)