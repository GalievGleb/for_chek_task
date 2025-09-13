"""Тут будут находиться все локаторы для дальнейшего использования"""


class LoginSelectors:
    """Селекторы на странице авторизации"""

    USERNAME_SELECTOR = '[id="user-name"]'
    PASSWORD_SELECTOR = '[id="password"]'
    BUTTON_LOGIN_SELECTOR = '#login-button'

    """Логин и пароль для авторизации"""
    LOGIN = "standard_user"
    PASSWORD = "secret_sauce"


class InventorySelectors:
    """Селекторы на странице товаров

    ADD_TO_BackPack_CARD_SELECTOR: Кнопка для добавления товара Backpack в корзину
    SHOPPINK_CART_LINK_SELECTOR: Кнопка корзины
    PRODUCT_BikeLight_CARD_SELECTOR: Карточка товара Bike Light
    """

    ADD_TO_BackPack_CARD_SELECTOR = "#add-to-cart-sauce-labs-backpack"
    SHOPPINK_CART_LINK_SELECTOR = "#shopping_cart_container"
    PRODUCT_BikeLight_CARD_SELECTOR = '.inventory_item a:has-text("Sauce Labs Bike Light")'


class BikeLightCardSelectors:
    """Селекторы на странице карточки товара Backpack

    ADD_TO_CARD_SELECTOR: Кнопка для добавления Bike Light в корзину
    SHOPPINK_CART_LINK_SELECTOR: Кнопка корзины
    """

    ADD_TO_CARD_SELECTOR = '#add-to-cart'
    SHOPPINK_CART_LINK_SELECTOR = "#shopping_cart_container"


class MyCartSelectors:
    """Селекторы на старнице Корзины"""

    CART_LIST_SELECTOR = '[class="cart_list"]'
    CONTINUE_SHOPPING_LOCATOR = '#continue-shopping'
    CHECKOUT_LOCATOR = '[id="checkout"]'
    # FIRST_ITEM_LOCATOR = '.cart_list div:has-text("Sauce Labs Backpack")'
    # SECOND_ITEM_LOCATOR = '.cart_list div:has-text("Sauce Labs Bike Light")'


class CheckoutSelectors:
    """Селекторы в Checkout"""

    CHECKOUT_INFO_SELECTOR = '[class="checkout_info"]'
    FIRST_NAME_SELECTOR = '[placeholder="First Name"]'
    SECOND_NAME_SELECTOR = '[placeholder="Last Name"]'
    ZIP_SELECTOR = '[placeholder="Zip/Postal Code"]'
    BUTTON_CONTINUE_SELECTOR = '[id="continue"]'
    BUTTON_FINISH_SELECTOR = '#finish'
    BUTTON_OPEN_MENU_SELECTOR = 'button:has-text("Open Menu")'
    BUTTON_LOGOUT_SELECTOR = '#logout_sidebar_link'
