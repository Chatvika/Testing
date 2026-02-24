"""
Selenium code using explicit wait to open Google and search for 'Python'
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Open Google
        driver.get("https://www.google.com/")
        
        # Wait for the search box to be visible
        # Using explicit wait with WebDriverWait
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        
        # Enter "Python" in the search box
        search_box.send_keys("Python")
        
        # Submit the search
        search_box.submit()
        
        # Wait for the results page to load
        # Wait for the search results container to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        print("Search completed successfully for 'Python'!")
        print(f"Page title: {driver.title}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the browser after a short delay to see the results
        input("Press Enter to close the browser...")
        driver.quit()


if __name__ == "__main__":
    main()


"""
Selenium code using explicit wait to open Google and search for 'java online compiler'
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Open Google
        driver.get("https://www.google.com/")
        
        # Wait for the search box to be visible
        # Using explicit wait with WebDriverWait
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        
        # Enter "java online compiler" in the search box
        search_box.send_keys("python selenium tutorial")
        
        # Submit the search
        search_box.submit()
        
        # Wait for the results page to load
        # Wait for the search results container to be visible
        WebDriverWait(driver, 5).until(
            EC.title_contains("java")((By.ID, "search"))
        )
        
        print("Search completed successfully for 'python selenium tutorial'!")
        print(f"Page title: {driver.title}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the browser after a short delay to see the results
        input("Press Enter to close the browser...")
        driver.quit()


if __name__ == "__main__":
    main()


