from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    #Locating Full Name Element and Its Parent
    full_name = driver.find_element(By.ID, "userName")
    find_parent = driver.find_element(By.XPATH, "//input[@id='userName']/parent::div")
    print(find_parent.get_attribute("class"))

    #Switching to Buttons Tabs
    driver.execute_script("window.open('https://demoqa.com/radio-button', '_blank');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    #Locating Yes Radio Button and Its Sibling
    yes_button= driver.find_element(By.XPATH, "//input[@id='yesRadio']")
    sibling_label = yes_button.find_element(By.XPATH, "following-sibling::label")
    print(sibling_label.text)

    #Switching to Checkbox Tab
    driver.execute_script("window.open('https://demoqa.com/checkbox', '_blank');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[2])

    #Locating Home Element and Spans Inside It
    home_element = driver.find_element(By.XPATH, "//label[@for='tree-node-home']")
    home_spans=home_element.find_elements(By.XPATH, ".//span")
    number_spans=len(home_spans)
    print(number_spans)
    for span in home_spans:
        print(span.get_attribute("class")) #To make sure only the spans inside the elements were selected
finally:
    driver.quit()