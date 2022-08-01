import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SearchCustomer:
    # search customer page
    txt_email_id = "SearchEmail"
    txt_first_name_id = "SearchFirstName"
    txt_last_name_id = "SearchLastName"
    btn_search_id = "search-customers"

    table_search_result_xpath = "//table[@id='customers-grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def set_first_name(self, fname):
        self.driver.find_element(By.ID, self.txt_first_name_id).clear()
        self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element(By.ID, self.txt_last_name_id).clear()
        self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(lname)

    def click_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def get_number_of_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def get_number_of_columns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1, self.get_number_of_rows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            email_id = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, name_to_search):
        flag = False
        for r in range(1, self.get_number_of_rows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name_searched = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name_searched == name_to_search:
                flag = True
                break
        return flag
