from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class ManageCustomer:

    def add_customer(self, LoginPage):
        """Perform the add customer action."""
        add_button = self.browser.find_element(By.XPATH,"//a[normalize-space()='Add']").click()

