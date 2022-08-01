import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class TestLoginDDT002:
    baseURL = ReadConfig.get_application_url()
    path = "TestData/LoginData.xlsx"

    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********** TestLoginDDT002 **********")
        self.logger.info("********** Verifying Login Page DDT Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.get_row_count(self.path, 'Sheet1')
        print("Number of rows in Excel : ", self.rows)

        lst_status = []
        for r in range(2, self.rows+1):
            self.username = XLUtils.read_data(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.read_data(self.path, 'Sheet1', r, 3)

            self.lp.set_user_name(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            self.act_title = self.driver.title
            self.exp_title = "Dashboard / nopCommerce administration"

            if self.act_title == self.exp_title:
                if self.exp == "Pass":
                    self.logger.info("****** Passed *******")
                    self.lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****** Failed *******")
                    self.lp.click_logout()
                    lst_status.append("Fail")
            elif self.act_title != self.exp_title:
                if self.exp == "Pass":
                    self.logger.info("****** Failed *******")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("****** Passed *******")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("****** Login DDT Test Passed *********")
            self.driver.close()
            assert True
        else:
            self.logger.info("****** Login DDT Test Failed *********")
            self.driver.close()
            assert False

        self.logger.info("****** End of Login DDT Test *********")
        self.logger.info("****** Completed TestLoginDDT002  *********")
