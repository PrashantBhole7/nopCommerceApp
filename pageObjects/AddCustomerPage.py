import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer page
    lnk_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_customer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_xpath = "//a[@class='btn btn-primary']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_first_name_xpath = "//input[@id='FirstName']"
    txt_last_name_name = "//input[@id='LastName']"
    rd_male_gender_id = "Gender_Male"
    rd_female_gender_id = "Gender_Female"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_company_name_xpath = "//input[@id='Company']"
    ch_btn_is_tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    txt_news_letter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    list_item_your_store_name_xpath = "//span[normalize-space()='Your store name']"
    list_item_test_store_2_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    txt_customer_role_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    list_item_Registered_xpath = "//span[normalize-space()='Registered']"
    list_item_Administarator_xpath = "////span[normalize-space()='Administrators']"
    list_item_forum_moderater_xpath = "//span[normalize-space()='Forum Moderators']"
    list_item_guests_xpath = "//li[contains(text(), 'Guests')]"
    list_item_vendors_xpath = "//li[contains(text(), 'Vendors')]"
    drp_manager_of_vendor_xpath = "//select[@id='VendorId']"
    txt_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer_menu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_xpath).click()

    def click_on_customer_menu_item(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menuitem_xpath).click()

    def click_on_add_new(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def set_passowrd(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def set_first_name(self, fname):
        self.driver.find_element(By.XPATH, self.txt_first_name_xpath).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element(By.XPATH, self.txt_last_name_name).send_keys(lname)

    def set_dob(self, dob):
        self.driver.find_element(By.XPATH, self.txt_dob_xpath).send_keys(dob)

    def set_company_name(self, com_name):
        self.driver.find_element(By.XPATH, self.txt_company_name_xpath).send_keys(com_name)

    def set_customer_role(self, role):
        self.driver.find_element(By.XPATH, self.txt_customer_role_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_Registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_Administarator_xpath)
        elif role == "Guests":
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_guests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_vendors_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_forum_moderater_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_guests_xpath)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def set_news_letter(self, news_letter):
        self.driver.find_element(By.XPATH, self.txt_news_letter_xpath).click()
        time.sleep(3)
        if news_letter == "Your store name":
            self.listitem_news = self.driver.find_element(By.XPATH, self.list_item_your_store_name_xpath)
        elif news_letter == "Test store 2":
            self.listitem_news = self.driver.find_element(By.XPATH, self.list_item_test_store_2_xpath)
        else:
            self.listitem_news = self.driver.find_element(By.XPATH, self.list_item_your_store_name_xpath)
        self.driver.execute_script("arguments[0].click();", self.listitem_news)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rd_male_gender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rd_female_gender_id).click()
        else:
            self.driver.find_element(By.ID, self.rd_male_gender_id).click()

    def set_manager_of_vendors(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_manager_of_vendor_xpath))
        drp.select_by_visible_text(value)

    def set_is_tax_exempt(self):
        self.driver.find_element(By.XPATH, self.ch_btn_is_tax_exempt_xpath).click()

    def set_admin_comment(self, content):
        self.driver.find_element(By.XPATH, self.txt_admin_comment_xpath).send_keys(content)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
