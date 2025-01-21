#Script for the adding menu item in the restaurant

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class RestaurantAdmin:
    def __init__(self):  # Default constructor
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Implicit wait for all elements

    def open_browser(self):
        self.driver.get("https://eatanceqaadminpanel.eatanceapp.com/backoffice/login")

    def login(self, em, password):  # Here we've pass the arguments
        self.driver.find_element(By.NAME, "email").send_keys(em)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "login_submit").click()

    def menu(self):
        wait = WebDriverWait(self.driver, 10)  # Explicit wait instance

        # Navigate to the menu section
        self.driver.find_element(By.XPATH, "//*[@id='sideMenu']").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/aside/ul/li[4]/a/span"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/aside/ul/li[4]/ul/li[2]/a/span"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add Menu Item']"))).click()

        # Fill the form with generated random strings
        def generate_random_string(length=10):
            return ''.join(random.choices(string.ascii_letters, k=length))

        def generate_random_digits(length=3):
            return ''.join(random.choices(string.digits, k=length))

        # Fill out item name and price
        self.driver.find_element(By.NAME, "item_name").send_keys(generate_random_string(6))
        self.driver.find_element(By.NAME, "price").send_keys(generate_random_digits(3))

        # Menu dropdown
        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[4]/div[1]/div/div/div/p").click()
        self.driver.find_element(By.XPATH, "//div[@class='SumoSelect sumo_menu open']//p[@class='select-all']").click()

        # Scroll down and select Menu Category
        self.driver.execute_script("window.scrollBy(0, 2000);")
        self.driver.find_element(By.XPATH, "//div[@class='SumoSelect sumo_category_id']//p[contains(@title,'Select')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add_edit_form']/div[4]/div[2]/div/div/div/div/ul/li[2]/label"))).click()

        # Menu Group dropdown
        self.driver.execute_script("window.scrollBy(0, 2000);")
        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[5]/div[1]/div/div/div/p").click()
        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[5]/div[1]/div/div/div/div/p[1]").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 1500);")


        # SKU field
        self.driver.find_element(By.ID, "sku").send_keys(generate_random_string())
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 600);")


        # Stock Status dropdown
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[6]/div[2]/div/div/div/p").click()
        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[6]/div[2]/div/div/div/div/ul/li[2]/label").click()
        self.driver.execute_script("window.scrollBy(0, 1500);")


        # Preparation Type
        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[13]/div[2]/div/div/div/p").click()
        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[13]/div[2]/div/div/div/div/ul/li[3]/label").click()

        # Food Types
        self.driver.find_element(By.XPATH, "//div[@class='SumoSelect sumo_food_type']//p[contains(@title,'Select')]").click()
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Veg']").click()
        self.driver.execute_script("window.scrollBy(0, 600);")


        # Availability
        self.driver.find_element(By.XPATH, "//*[@id='availability1']").click()

        # Description and Ingredients
        self.driver.execute_script("window.scrollBy(0, 600);")

        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[15]/div[1]/div/textarea").send_keys(generate_random_string())
        self.driver.find_element(By.XPATH, "//*[@id='add_edit_form']/div[15]/div[2]/div/textarea").send_keys(generate_random_string())

        # Display Order
        self.driver.find_element(By.ID, "sort_order").send_keys("5")

        # Submit the form
        submit_button = self.driver.find_element(By.XPATH, "(//button[@id='submitForm'])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='submitForm'])[1]"))).click()

    print("Item has been added successfully")


# Function calling
obj = RestaurantAdmin()  # Create the object of the RestaurantAdmin class
obj.open_browser()
obj.login("ceo@yopmail.com", "Test@123")
obj.menu()
