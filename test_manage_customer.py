import pytest
from utils.browser import get_browser
from pages.login_page import LoginPage
from pages.manage_customer import ManageCustomer
import time

@pytest.fixture
def browser():
    driver = get_browser()
    yield driver
    driver.quit()

@pytest.fixture
def login(browser):
    """Fixture to log in to the application."""
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("hiteshkumar@evincedev.com", "Test@123")
    time.sleep(2)  # Wait for the login to complete
    return browser

@pytest.fixture
def manage_customer_page(login):
    """Fixture to return the ManageCustomerPage instance after login."""
    return ManageCustomer(login)

def test_add_customer(manage_customer_page):
    """Test adding a new customer."""
    manage_customer_page.navigate_to_manage_customers()
    manage_customer_page.add_customer("John Doe", "john.doe@example.com")
    time.sleep(2)

    # Verify the customer was added
    customer_list = manage_customer_page.get_customer_list()
    assert "John Doe" in customer_list, "Customer not added successfully"

