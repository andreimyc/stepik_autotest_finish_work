from selenium import webdriver
from selenium.webdriver import Remote as RemoteWebDriver


class BasePage():
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url

    def open(self):
        browser = webdriver.Chrome()
        self.browser.get(self.url)
