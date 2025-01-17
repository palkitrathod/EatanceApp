import os
import sys
from selenium import webdriver

def get_browser():
    #setup the browser
    sys.stdout = open(os.devnull, 'w')
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
