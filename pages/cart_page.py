from utils.locators import *
from pages.base_page import BasePage


class CartPase(BasePage):

    def __init__(self, driver):
        self.locator = MainPageLocators
        super(CartPase, self).__init__(driver)  # Python2 version

    def click_icon_delete(self):
        self.find_element(*self.locator.DELETE_IN_CART).click()

