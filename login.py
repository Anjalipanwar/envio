#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:11:20 2019

@author: anjalip
"""

#Login using Selenium in Chrome

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from config import config
from config import login_input 
import logger

class UIloginSuite():

    def init_browser(self):    
    
        logger.logger.info('Open chrome')
        self.driver = webdriver.Chrome()
        
        logger.logger.info('Open website')
        self.driver.get(config.URL)
        
        time.sleep(2)
    
    def login(self):
    
        logger.logger.info("Navigate to Login Page by clicking Sign in")
        
        signin = self.driver.find_element_by_xpath(login_input.signin)
        signin.send_keys(Keys.RETURN)
        
        logger.logger.info("Enter email")
        email = self.driver.find_element_by_xpath(login_input.email_input)
        email.send_keys(config.EMAIL)
        #email.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        logger.logger.info("Enter Password")
        pwrd = self.driver.find_element_by_xpath('/html/body/app-root/app-auth-page/div/div/div/div/form/fieldset/fieldset[3]/input')
        pwrd.seself.nd_keys(config.PASSWORD)
        
        logger.logger.info("Hit Enter to click Sing in button")
        pwrd.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        logger.logger.info("Navigate to Settings")
        settings = self.driver.find_element_by_xpath('/html/body/app-root/app-layout-header/nav/div/ul/li[3]/a')
        settings.click()
        
    def logout(self):
        

        logger.logger.info("Click logout")
        logout = self.driver.find_element_by_xpath('/html/body/app-root/app-settings-page/div/div/div/div/button')
        logout.click()
        
        time.sleep(2)

    def shut_driver(self):
        
        self.driver.close()
        
if __name__ == '__main__': 
    
    logger.logger.info("Execution Starts here..")
    uiloginsuite_obj = UIloginSuite()

    
    uiloginsuite_obj.init_browser()
    
    

