from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    LOGO = (By.CLASS_NAME, 'Header_LogoImg__cvLy8')
    ACCOUNT = (By.CLASS_NAME, 'Header_ActionUser__AHnWb')
    SIGNUP = (By.CLASS_NAME, 'signup')
    LOGIN = (By.CLASS_NAME, 'Header_ActionUser__Cf44s')
    SEARCH = (By.CLASS_NAME, 'input_search')
    SEARCH_BUTTON = (By.CLASS_NAME, 'Header_SearchBtn__5wt0m')
    # HELP_LINK = (By.XPATH, '//a[text()=\'Help\']')
    DETAIL = (By.CLASS_NAME, 'product_trainding')
    ADD_CART = (By.ID, 'add_cart')
    ICON_CART = (By.ID, 'icon_cart')
    DELETE_IN_CART = (By.ID, 'delete_cart')


class ProductPageLocators(object):
    PRODUCT = (By.CLASS_NAME, 'sanpham')
    SEARCH = (By.CLASS_NAME, 'input_search')
    SEARCH_BUTTON = (By.CLASS_NAME, 'Header_SearchBtn__5wt0m')
    CAMHUNG = (By.ID, 'camhung')
    BANHANG = (By.ID, 'banhang')
    BIAN = (By.ID, 'bian')
    LOGIN = (By.CLASS_NAME, 'Header_ActionUser__AHnWb')



class LoginPageLocators(object):
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.CLASS_NAME, 'submit')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-container')

# class HelpPageLocators(object):
#     HELPSEARCH = (By.XPATH, '//input[@id=\'helpsearch\']')
#     PAYMENTMETHODTEXT = (By.XPATH, '// h2[contains(text(), \'Manage Payment Methods\')]')






