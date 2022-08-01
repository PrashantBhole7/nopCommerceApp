import time
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class TestSearchCustomer005:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("********** TestSearchCustomer005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)

        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Search Customer By Name **********")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customer_menu()
        self.add_cust.click_on_customer_menu_item()

        self.logger.info("********** Searching customer by name **********")

        search_cust = SearchCustomer(self.driver)
        search_cust.set_first_name("Victoria")
        search_cust.set_last_name("Terces")
        search_cust.click_search()
        status = search_cust.search_customer_by_name("Victoria Terces")
        assert True == status

        self.logger.info("********** TestSearchCustomer005 Completed **********")
        self.driver.close()
