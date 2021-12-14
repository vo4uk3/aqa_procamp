
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class Chrome():

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        

class Firefox():

    def __init__(self):
        self.driver = webdriver.Firefox(GeckoDriverManager().install())


class Driver():

    BROWSERS = {

        'chrome' : Chrome(),
        'firefox' : Firefox()
    }

    def __init__(self, browser):
        self.browser = Driver.BROWSERS.get(browser)



