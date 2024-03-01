
import unittest
import sys
sys.path.append('D:/Testing/test_selenium_cho_book_shop')
from base_test import BaseTest
from pages.main_page import *
from pages.cart_page import *
from utils.test_cases import test_cases
import time


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestSignInPage(BaseTest):

    def test_page_load(self):
        print("\n" + str(test_cases(10)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())
    
    def test_sign_in_button(self):
        print("\n" + str(test_cases(4)))
        page = MainPage(self.driver)
        login_page = page.click_sign_in_button()

    def test_sign_up_button(self):
        print("\n" + str(test_cases(3)))
        page = MainPage(self.driver)
        sign_up_page = page.click_sign_up_button()
        self.assertIn("/register", sign_up_page.get_url())


    # def test_search_item(self):
    #     print("\n" + str(test_cases(1)))
    #     page = MainPage(self.driver)
    #     self.driver.save_screenshot('BeforeSearch.png')
    #     search_result = page.search_item("Thỏ")
    #     self.driver.save_screenshot('AfterSearch.png')
    #     self.assertIn("/sanpham", search_result)
        

    # def test_sign_in_with_valid_user(self):
    #     print("\n" + str(test_cases(2)))
    #     main_page = MainPage(self.driver)
    #     login_page = main_page.click_sign_in_button()
    #     result = login_page.login_with_valid_user("valid_user")


    # def test_sign_in_with_in_valid_user(self):
    #     print("\n" + str(test_cases(5)))
    #     main_page = MainPage(self.driver)
    #     login_page = main_page.click_sign_in_button()
    #     result = login_page.login_with_in_valid_user("invalid_user")
    #     self.assertIn("Bạn Chưa Nhập Mật Khẩu Đúng", result)
    
    # def test_click_product(self):
    #     print("\n" + str(test_cases(6)))
    #     page = MainPage(self.driver)
    #     detail_page = page.detail_product_click()

    #  def test_add_to_cart(self):
    #     print("\n" + str(test_cases(7)))
    #     page = MainPage(self.driver)
    #     detail_page = page.detail_product_click()
    #     add = page.click_add_cart()

    #  def test_navigate_cart(self):
    #     print("\n" + str(test_cases(8)))
    #     page = MainPage(self.driver)
    #     cart = page.click_icon_cart()

    #  def test_delete_product_in_cart(self):
    #     print("\n" + str(test_cases(9)))
    #     page = MainPage(self.driver)
    #     cart = page.click_icon_cart()
    #     delete = page.click_icon_delete()
    
    # def test_add_cart(self):
    #     print("\n" + str(test_cases(5)))
    #     main_page = MainPage(self.driver)
    #     cart = main_page.detail_product_click()
    #     add = main_page.click_add_cart()
       
  