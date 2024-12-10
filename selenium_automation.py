from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Use webdriver-manager to handle the chromedriver installation
    service = Service(ChromeDriverManager().install())  # Installs the chromedriver automatically

    # Initialize Chrome driver
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def capture_screenshot(driver, filename):
    driver.save_screenshot(filename)

def main():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)
    url = "https://inc42.com/"  # Replace with your target URL
    email = "your_email@example.com"  # Replace with actual login credentials
    password = "your_password"  # Replace with actual password

    try:
        driver.get(url)
        print("Navigated to the website")

        # Additional automation steps (e.g., login, click buttons, etc.)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
