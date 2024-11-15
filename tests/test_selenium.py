from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_google_search():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("GitHub Actions")
        search_box.submit()
        time.sleep(2)  # Allow time for results to load

        # Validate that results are loaded by checking for a specific element
        assert "GitHub Actions" in driver.page_source
    finally:
        driver.quit()

if __name__ == "__main__":
    test_google_search()
