from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
import time


def run_test(driver):
    try:
        driver.get("https://www.armstqb.org/")
        driver.maximize_window()
        print("Page 1 URL:", driver.current_url)
        print("Page 1 Title:", driver.title)

        # Opening and switching to a new tab
        driver.execute_script("window.open('https://www.armstqb.org/partners', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        print("Page 2 URL:", driver.current_url)
        print("Page 2 Title:", driver.title)

        time.sleep(2)
        driver.minimize_window()
        driver.close()
    finally:
        driver.quit()

# Running on Chrome
print("Running on Chrome:")
chrome_driver = webdriver.Chrome()
run_test(chrome_driver)

# Runnung on Edge
print("\nRunning on Edge:")
edge_driver = webdriver.Edge()
run_test(edge_driver)
# test comment
