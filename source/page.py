from selenium import webdriver
from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.common.by import By
from resources.config import Config


class Page:
    """
    A class to handle web pages under test
    """

    browser = {'chrome': Chrome, 'firefox': Firefox, 'edgd': Edge}
    exe_name = {'chrome': 'chromedriver.exe', 'firefox': 'geckodriver.exe', 'edge': 'msedgedriver.exe'}
    opts = {'chrome': webdriver.chrome, 'firefox': webdriver.firefox}

    def __init__(self, browser, url):
        self.url = Config.base_url+url
        self.opt = Page.opts[browser].options.Options()
        self.opt.add_argument('headless')
        self.driver = Page.browser[browser](executable_path='C:/Python39/Scripts/'+Page.exe_name[browser], options=self.opt)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def close_driver(self):
        self.driver.close()
