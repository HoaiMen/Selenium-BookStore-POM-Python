from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
# from pages.help_page import HelpPage
from utils.locators import *

class ProductBasePage(BasePage):
    def __init__(self, driver):
        self.locator = ProductPageLocators
        super().__init__(driver)

    def click_category_button(self):
        self.find_element(*self.locator.PRODUCT).click()
        self.find_element(*self.locator.CAMHUNG).click()
        self.find_element(*self.locator.BANHANG).click()
        self.find_element(*self.locator.BIAN).click()
        
    
    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        
    
    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click()


    def login_from_product_page(self, item):
        self.find_element(*self.locator.LOGIN).click()
