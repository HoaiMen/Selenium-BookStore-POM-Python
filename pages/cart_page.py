from utils.locators import *
from pages.base_page import BasePage


class CartPase(BasePage):

    def __init__(self, driver):
        self.locator = MainPageLocators
        super(CartPase, self).__init__(driver)  # Python2 version

    def click_icon_delete(self):
        self.find_element(*self.locator.DELETE_IN_CART).click()


    # def login(self, user):
    #     user = users.get_user(user)
    #     print(user)
    #     self.enter_email(user["email"])
    #     self.enter_password(user["password"])
    #     self.click_login_button()

    # def login_with_valid_user(self, user):
    #     self.login(user)
        

    # def login_with_in_valid_user(self, user):
    #     self.login(user)
    #     return self.find_element(*self.locator.ERROR_MESSAGE).text
