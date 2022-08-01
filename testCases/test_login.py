import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestLogin001:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.log_gen()

    @pytest.mark.sanity
    def test_home_page_title(self, setup):
        self.logger.info("********** TestLogin001 **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.act_title = self.driver.title
        if self.act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("********** Home Page Title Passed **********")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/" + "test_home_page_title.png")
            self.driver.close()
            self.logger.info("********** Home Page Title Failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********** TestLogin001 **********")
        self.logger.info("********** Verifying Login Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.act_title = self.driver.title
        if self.act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("********** Login Page Title Passed **********")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/" + "test_login_page_title.png")
            self.driver.close()
            self.logger.info("********** Login Page Title Failed **********")
            assert False
