from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """Initialize the login page with the browser instance."""
        self.browser = driver
        self.url = "https://eatanceqasuperadmin.eatanceapp.com/backend/home"

    def load(self):
        """Load the login page."""
        self.browser.get(self.url)

    def login(self, email, password):
        """Perform the login action."""
        email_field = self.browser.find_element(By.ID, "username")
        password_field = self.browser.find_element(By.ID, "password")
        submit_button = self.browser.find_element(By.NAME, "submit")

        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_button.click()
