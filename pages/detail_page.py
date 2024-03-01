from utils.locators import *
from pages.base_page import BasePage
from utils import users


class DetailPase(BasePage):

    def __init__(self, driver):
        self.locator = MainPageLocators
        super(DetailPase, self).__init__(driver)  # Python2 version


    def detail_product_click_add_cart(self):
        self.detail_product_click()
        self.find_element(*self.locator.ADD_CART).click()