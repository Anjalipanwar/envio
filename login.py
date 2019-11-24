#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:11:20 2019

@author: anjalip
"""

# Gmail Login using Selenium in Firefox

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Open chrome
driver = webdriver.Chrome()

#Open website
driver.get("https://angular.realworld.io")

time.sleep(2)

#Navigate to Login Page by clicking Sign in

signin = driver.find_element_by_xpath('/html/body/app-root/app-layout-header/nav/div/ul/li[2]/a')
signin.send_keys(Keys.RETURN)

#Enter email
email = driver.find_element_by_xpath('/html/body/app-root/app-auth-page/div/div/div/div/form/fieldset/fieldset[2]/input')
email.send_keys('official.anjali@gmail.com')
#email.send_keys(Keys.RETURN)

time.sleep(2)

#Enter Password
pwrd = driver.find_element_by_xpath('/html/body/app-root/app-auth-page/div/div/div/div/form/fieldset/fieldset[3]/input')
pwrd.send_keys('testpass@123')

#Hit Enter to click Sing in button
pwrd.send_keys(Keys.RETURN)

time.sleep(2)

#Navigate to Settings
settings = driver.find_element_by_xpath('/html/body/app-root/app-layout-header/nav/div/ul/li[3]/a')
settings.click()

#Click logout
logout = driver.find_element_by_xpath('/html/body/app-root/app-settings-page/div/div/div/div/button')
logout.click()

time.sleep(2)

driver.close()