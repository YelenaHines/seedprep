# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:08:42 2019

@author: YHINE
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC
import time
import flaskblog.general_functions as gf
#import pyperclip

class OrionFunctions():

    orion= "http://w3.regsciweb.monsanto.com/Orion/OrionLogon"
    view_container = 'http://w3.regsciweb.monsanto.com/Orion/screens/createContainer/plant/plant_view.jsp'
    orion_request= 'http://w3.regsciweb.monsanto.com/Orion/screens/request/manageQueue/plant/manageQueue.jsp'

    capabilities = {
          'browserName': 'chrome',
          'chromeOptions':  {
            'useAutomationExtension': False,
            'forceDevToolsScreenshot': True,
            'args': ['--start-maximized', '--disable-infobars']
          }
        }

    driver = webdriver.Chrome(desired_capabilities=capabilities)
    matches = []

    def __init__(self, username, password, request_id=None):
        self.username = username
        self.password = password
        self.request_id = request_id
#        self.driver = webdriver.Remote(command_executor='http://10.127.178.42:5000/login_1', desired_capabilities=self.capabilities)

    def logon_orion(self):
        self.driver.get(self.orion)
    #    driver.set_window_size(1000, 500)
        self.driver.find_element_by_name("j_username").clear()
        self.driver.find_element_by_name("j_username").send_keys(self.username)
        self.driver.find_element_by_name("j_password").send_keys(self.password)
        self.driver.find_element_by_class_name("button").click()


    def get_requests(self):
        self.driver.get(self.orion_request)
        self.driver.find_element_by_id("pend").click()
        self.driver.find_element_by_id("ship").click()
        self.driver.find_element_by_id("prog").click()
        self.driver.find_element_by_id("appr").click()
        self.driver.find_element_by_id("updateButton").click()

    def get_request_id(self, request_id):

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'requestId_{}'.format(self.request_id))))
            self.driver.find_element_by_id('requestId_{}'.format(self.request_id)).click()
        except NoSuchElementException:
            return False

    def open_shipTrans(self):
#    find_shiptrans = driver.find_element_by_id('viewShipmentButton')
        time.sleep(3)
        self.driver.find_element_by_id('viewShipmentButton').click()
        time.sleep(1)
        #select all containers
        select = Select(self.driver.find_element_by_id('viewSamplesTopPageSelector'))
        select.select_by_value('all')

        self.driver.find_element_by_id('viewSamples_monNumbers_link').click()

        time.sleep(1)

        gf.select_all()
        gf.copy()

        time.sleep(1)

    def paste_container(self, matches):
    #orionIDs is a list of orion ids needing to be viewed
        time.sleep(2)
        self.driver.get(self.view_container)
        for i in self.matches:
            time.sleep(1)
            self.driver.find_element_by_id("containerSelectorTableContainerIdInput").send_keys(
                    i, Keys.ENTER)
            time.sleep(2)
        self.matches = []

    def close_driver(self):
        self.driver.close
