# 抓取网页
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(
    r"D:\dfh\chromedriver\chromedriver.exe"
)
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
chrome = webdriver.Chrome(service=service,options=chrome_options)

chrome.get("https://quotes.toscrape.com/")
print(chrome.title)