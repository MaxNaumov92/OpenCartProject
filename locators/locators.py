from selenium.webdriver.common.by import By


class BasePageLocators:
    # ----------------------HEADER------------------------------------------------------------------
    # CURRENCY SETTINGS
    CURRENCY_BUTTON_DROPDOWN = (By.CSS_SELECTOR, '.btn.btn-link.dropdown-toggle')
    CURRENCY_BUTTON_EURO = (By.NAME, "EUR")
    CURRENCY_BUTTON_POUND_STERLING = (By.NAME, "GBR")
    CURRENCY_BUTTON_US_DOLLAR = (By.NAME, "USD")
    # CONTACT US
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, '.fa.fa-phone')
    # MY ACCOUNT(LOGIN\REG)
    MY_ACCOUNT_BUTTON_DROPDOWN = (By.CSS_SELECTOR, '.fa.fa-user')
    MY_ACCOUNT_REGISTER_BUTTON = (By.XPATH, '//a[text() = "Register"]')
    MY_ACCOUNT_LOGIN_BUTTON = (By.XPATH, '//a[text() = "Login"]')
    MY_ACCOUNT_MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '.dropdown [title="My Account"]')
    # WISH LIST
    WISH_LIST_BUTTON = (By.ID, 'wishlist-total')
    # CART
    CART_ICON_BUTTON = (By.CSS_SELECTOR, "[title='Shopping Cart']")
    # CHECKOUT
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'strong .fa.fa-share')
    # ------------------------SEARCH-------------------------------------------------------------------
    SEARCH_TEXT_HOLDER = (By.CSS_SELECTOR, '.form-control.input-lg')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.btn.btn-default.btn-lg .fa')
    # ------------------------CART IMAGE BLACK BUTTON--------------------------------------------------
    CART_BIG_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle')
    CART_ITEMS_AND_TOTAL_COST = (By.CSS_SELECTOR, "#cart-total")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#cart .text-center')
    # ----------------------------NAVBAR CATEGORIES----------------------------------------------------
    NAVBAR_HOME_BUTTON = (By.CSS_SELECTOR, '.fa.fa-home')
    NAVBAR_DESKTOPS_BUTTON_DROPDOWN = '.dropdown-toggle[href="http://localhost/desktops"]'
    NAVBAR_DESKTOPS_PC_BUTTON = (By.CSS_SELECTOR, '#menu [href="http://localhost/desktops/pc"]')
    NAVBAR_DESKTOPS_MAC_BUTTON = (By.CSS_SELECTOR, '#menu [href="http://localhost/desktops/mac"]')
    NAVBAR_DESKTOPS_SHOW_ALL_BUTTON = (By.CSS_SELECTOR, '.see-all[href="http://localhost/desktops"]')
    # -----------------------------FOOTER------------------------------------------------------------------
    # INFORMATION
    ABOUT_US = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/about_us"]')
    DELIVERY_INFO = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/delivery"]')
    PRIVACY_POLICY = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/privacy"]')
    TERMS_AND_CONDITIONS = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/terms"]')
    # CUSTOMER SERVICE
    CONTACT_US = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=information/contact"]')
    RETURNS = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=account/return/add"]')
    SITE_MAP = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=information/sitemap"]')
    # EXTRAS
    BRANDS = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=product/manufacturer"]')
    GIFT_CERTIFICATES = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=account/voucher"]')
    AFFILIATE = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=affiliate/login"]')
    SPECIALS = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=product/special"]')
    # MY_ACCOUNT
    MY_ACCOUNT_FOOTER = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=account/account"]')
    ORDER_HISTORY = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=account/order"]')
    WISH_LIST_FOOTER = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=account/wishlist"]')
    NEWSLETTER = (By.CSS_SELECTOR, '.col-sm-3 [href="http://localhost/index.php?route=account/newsletter"]')
    OPENCART_URL_FOOTER = (By.CSS_SELECTOR, '.container [href="http://www.opencart.com"]')


class UserTableLocators:
    # Table available from Login, Register, My Account and Wishlist pages
    LOGIN_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/login"]')
    REGISTER_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/register"]')
    FORGOTTEN_PASS_2 = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/forgotten"]')
    MY_ACCOUNT_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/account"]')
    ADDRESS_BOOK_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/address"]')
    WISH_LIST_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/wishlist"]')
    ORDER_HISTORY_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/order"]')
    DOWNLOADS_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/download"]')
    RECURRING_PAYMENTS_CELL = \
        (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/recurring"]')
    REWARD_POINTS_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/reward"]')
    RETURNS_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/return"]')
    TRANSACTIONS_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/transaction"]')
    NEWSLETTER_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/newsletter"')


class LoginPageLocators(UserTableLocators):
    REG_ACC_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.well [href="http://localhost/index.php?route=account/register"]')
    EMAIL_HOLDER = (By.ID, 'input-email')
    PASSWORD_HOLDER = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[value="Login"].btn.btn-primary')
    FORGOTTEN_PASS_1 = (By.CSS_SELECTOR, '.form-group [href="http://localhost/index.php?route=account/forgotten"]')
    LOGIN_WARNING_PASS_OR_EMAIL = (By.CSS_SELECTOR, 'fa fa-exclamation-circle')
    LOGOUT_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/logout"]')


class AccountPageLocators(UserTableLocators):

    LOGOUT_CELL = (By.CSS_SELECTOR, '#column-right [href="http://localhost/index.php?route=account/logout"]')


class RegisterPageLocators:
    FIRST_NAME_HOLDER = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_HOLDER = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_HOLDER = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE_HOLDER = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_HOLDER = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM_HOLDER = (By.CSS_SELECTOR, "#input-confirm")
    SUBSCRIBE_RADIO_BTN_YES = (By.CSS_SELECTOR, ".radio-inline [value='1']")
    SUBSCRIBE_RADIO_BTN_NO = (By.CSS_SELECTOR, ".radio-inline [value='0']")
    PRIVACY_POLICE_CHECK_FIELD = (By.CSS_SELECTOR, ".pull-right [name='agree']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary[value='Continue']")
