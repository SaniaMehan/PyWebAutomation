from selenium.webdriver.common.by import By
import time


class KatalonHomePage():

    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    make_appointment = (By.ID, "btn-make-appointment")

    # Return a WebElement ->  username
    def get_make_appointment(self):
        return self.driver.find_element(*KatalonHomePage.make_appointment)

    # Page Actions

    def click_homepage(self):
        time.sleep(3)
        self.get_make_appointment().click()

    # def click_homepage(self,username):
    #     time.sleep(3)
    #     self.get_make_appointment().click()