import pytest
from utils.browser import get_browser  # Browser utility for setup
from pages.login_page import LoginPage  # LoginPage class for POM
import time

# Define URL in one place
HOME_URL = "https://eatanceqasuperadmin.eatanceapp.com/backend/home"

@pytest.fixture
def browser():
    """Fixture to initialize and quit the browser."""
    driver = get_browser()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(browser):
    """Fixture to return a LoginPage instance."""
    page = LoginPage(browser)
    page.load()
    return page

# Test cases
def test_valid_login(login_page):
    """Test case for valid login."""
    login_page.login("hiteshkumar@evincedev.com", "Test@123")
    time.sleep(3)  # Wait for page load
    print(f"After valid login, current URL: {login_page.browser.current_url}")

def test_invalid_email(login_page):
    """Test case for invalid email."""
    login_page.login("test@yopmail.com", "Test@123")
    time.sleep(3)  # Wait for page load
    print(f"After invalid email login, current URL: {login_page.browser.current_url}")

def test_invalid_password(login_page):
    """Test case for invalid password."""
    login_page.login("hiteshkumar@evincedev.com", "wrongpassword")
    time.sleep(3)  # Wait for page load
    print(f"After invalid password login, current URL: {login_page.browser.current_url}")

def test_invalid_email_password(login_page):
    """Test case for invalid email and password."""
    login_page.login("hiteshkumar@e@vincedev.com", "wrongpassword")
    time.sleep(3)  # Wait for page load
    print(f"After invalid email and password login, current URL: {login_page.browser.current_url}")

def test_blank_login(login_page):
    """Test case for blank login credentials."""
    login_page.login("   ", "   ")
    time.sleep(3)  # Wait for page load
    print(f"After blank login, current URL: {login_page.browser.current_url}")

def test_blank_email(login_page):
    """Test case for blank email."""
    login_page.login("", "Test@123")
    time.sleep(3)  # Wait for page load
    print(f"After blank email login, current URL: {login_page.browser.current_url}")

def test_blank_password(login_page):
    """Test case for blank password."""
    login_page.login("hiteshkumar@evincedev.com", "")
    time.sleep(3)  # Wait for page load
    print(f"After blank password login, current URL: {login_page.browser.current_url}")
