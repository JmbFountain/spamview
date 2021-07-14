#!/usr/bin/env python3
from selenium import webdriver
from werkzeug.utils import secure_filename


driverOptions = webdriver.FirefoxOptions()
driverOptions.set_headless(True)
driver = webdriver.Remote(command_executor='http://selenium:4444/wd/hub', options=driverOptions)


def getScreenshot(url, sessionPath):
    driver.get(url)
    full_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    full_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(full_width, full_height)
    imagePath = sessionPath + secure_filename(driver.title)
    driver.find_element_by_tag_name('body').screenshot(imagePath)
    driver.quit()


if '__name__' == '__main__'
    getScreenshot("https://www.heise.de", "../../session/")