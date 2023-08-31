import unittest
from pages.product_page import ProductBasePage
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases



class TestProductPage (BaseTest): 
    
    def test_search_item(self):
        print("\n" + str(test_cases(0)))
        page = ProductBasePage(self.driver)
        self.driver.save_screenshot('BeforeSearch.png')
        search_result = page.search_item('Tho')
        self.driver.save_screenshot('AfterSearch.png')
        

    def test_click_category_button(self):
        print("\n" + str(test_cases(1)))
        page = ProductBasePage(self.driver)
        self.driver.save_screenshot('BeforeClickSanPham.png')
        product_page = page.click_category_button()
        self.driver.save_screenshot('AfterClickSanPham.png')

    # def test_click_category_button(self):
    #     print("\n" + str(test_cases(2)))
    #     page = ProductBasePage(self.driver)
    #     login_page = page.login_from_product_page()


        
        
        
        