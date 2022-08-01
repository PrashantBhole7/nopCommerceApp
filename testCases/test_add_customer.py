import time
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class TestAddCustomer003:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.log_gen()

    @pytest.mark.sanity
    def test_add_customer(self, setup):
        self.logger.info("********** TestAddCustomer003 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)

        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Add Customer Test **********")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customer_menu()
        time.sleep(2)
        self.add_cust.click_on_customer_menu_item()
        self.add_cust.click_on_add_new()

        self.logger.info("********** Providing Customer Info **********")

        self.email = random_generator() + "@gmail.com"
        self.add_cust.set_email(self.email)
        self.add_cust.set_passowrd("test123")
        self.add_cust.set_first_name("Prashant")
        self.add_cust.set_last_name("Bhole")
        self.add_cust.set_gender("Male")
        self.add_cust.set_dob("7/08/1990")
        self.add_cust.set_company_name("BusyQA")
        self.add_cust.set_is_tax_exempt()
        self.add_cust.set_customer_role("Vendors")
        self.add_cust.set_news_letter("Test store 2")
        self.add_cust.set_manager_of_vendors("Vendor 2")
        self.add_cust.set_admin_comment("This is for testing......")
        time.sleep(8)
        self.add_cust.click_save()

        self.logger.info("********** Saving Customer Info **********")

        self.logger.info("********** Providing Customer Info **********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*********Add Customer Test is Passed********")
        else:
            self.driver.save_screenshot("Screenshots/" + "test_add_customer.png")
            self.logger.info("********** Login Page Title Failed **********")
            assert False

        self.driver.close()
        self.logger.info("********** Ending Add Customer Test **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))