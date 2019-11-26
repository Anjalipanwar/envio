#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:11:20 2019

@author: anjalip
"""

# Login using Selenium in Chrome

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from config import config
from config.config import login_input , login_validation
import logger


class UIloginSuite():

    def init_browser(self):
        logger.logger.info('Open chrome..')

        try:

            ####headless browser execution#######

            # options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            # self.driver = webdriver.Chrome(chrome_options = options, executable_path='/usr/local/bin/chromedriver')

            #####################################

            self.driver = webdriver.Chrome()
            logger.logger.info('Successfully opened chrome')
        except:
            logger.logger.info("Exception Occurred while opening chrome browser")

        logger.logger.info('Open website..')
        try:
            self.driver.get(config.URL)
            logger.logger.info('Successfully opened website')
        except:
            logger.logger.info("Exception Occurred while opening website")

        time.sleep(2)
        # try:
        #     self.login()
        # except:
        #     logger.logger.info("Exception Occurred while executing login method")

    def login(self):

        try:
            logger.logger.info("Navigate to Login Page by clicking Sign in..")
            signin = self.driver.find_element_by_xpath(login_input['signin'])
            signin.send_keys(Keys.RETURN)
        except:
            logger.logger.info("Failed to Navigate to Login Page by clicking Sign in")

        try:
            logger.logger.info("Enter email")
            email = self.driver.find_element_by_xpath(login_input['email_input'])
            email.send_keys(config.EMAIL)
        except:
            logger.logger.info("Failed to enter email address")

        time.sleep(2)

        try:
            logger.logger.info("Enter Password")
            pwrd = self.driver.find_element_by_xpath(login_input['password_input'])
            pwrd.send_keys(config.PASSWORD)
            logger.logger.info("Hit Enter to click Sing in button")
            pwrd.send_keys(Keys.RETURN)
        except:
            logger.logger.info("Failed to enter password")

        time.sleep(2)

        try:
            logger.logger.info('Validate Your Feed tab existence on successful login')
            element = self.driver.find_element(By.XPATH, login_input['your_feed'])
            text = element.text
            time.sleep(2)
            assert text == login_validation['home_page']
            logger.logger.info('Successfully logged in')
        except:
            logger.logger.info("Error occurred while sign in")

        # try:
        #     self.settings()
        # except:
        #     logger.logger.info("Error occurred while executing settings method")


    def settings(self):

        try:
            logger.logger.info("Navigate to Settings")
            settings = self.driver.find_element_by_xpath(login_input['settings'])
            settings.click()
        except:
            logger.logger.info("Failed to Navigate to Settings")

        # try:
        #     self.logout()
        # except:
        #     logger.logger.info("Error occurred while executing logout method")

    def logout(self):
        logger.logger.info("Click logout")

        try:
            logout = self.driver.find_element_by_xpath(login_input['logout'])
            time.sleep(2)
            logout.click()
        except:
            logger.logger.info("Error occurred while signing out ")

        # try:
        #     self.shut_driver()
        # except:
        #     logger.logger.info("Error occurred while executing shut_driver method")


    def shut_driver(self):
        try:
            logger.logger.info("Closing Chrome Browser")
            self.driver.close()
        except:
            logger.logger.info('Failed to close chrome browser')


if __name__ == '__main__':
    logger.logger.info("Execution Starts here..")
    uiloginsuite_obj = UIloginSuite()

    uiloginsuite_obj.init_browser()


