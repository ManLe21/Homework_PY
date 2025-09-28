from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Selecting Elements from Category Cards
    elements = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".category-cards")))
    cards = elements.find_elements(By.CSS_SELECTOR, "div.card.mt-4.top-card")

    if cards:
        card = cards[0]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.card.mt-4.top-card")))
        card.click()
    else:
        print("No cards found matching 'div.card.mt-4.top-card'")

    # Finding Buttons from the Elements Lists
    wait.until(EC.element_to_be_clickable((By.ID, "item-4"))).click()  #

    # Step 3: Click on "Click Me" button (not double-click or right-click)
    wait = WebDriverWait(driver, 10)
    click_me_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(@class, 'btn-primary') and normalize-space(text())='Click Me']"))
    ) #Selecting a button by Xpath and also Text
    click_me_btn.click()


    #Verifying that it is clicked
    click_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p#dynamicClickMessage")))
    print("Click Me button was successfully clicked.")

    # driver.save_screenshot("screenshot.png")
    # print("Screenshot saved as screenshot.png") Trying screenshot

    # Open new tab and navigate to radio button page
    driver.execute_script("window.open('https://demoqa.com/radio-button', '_blank');")
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])

    #Clicking on "Impressive" radio button
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='impressiveRadio']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    driver.execute_script("arguments[0].click();", element) #Added scroll so that the pop ups don't cover

    # Verify the button was selected
    result = driver.find_element(By.CLASS_NAME, "text-success")
    assert result.text == "Impressive"
    print("'Impressive' radio button was successfully selected.")
    driver.close()

    # Switching back to first tab
    driver.switch_to.window(driver.window_handles[0])

    # Go to "Links"
    driver.find_element(By.ID, "item-5").click()  # Links menu item

    # Find all links inside the page
    all_links = driver.find_elements(By.CSS_SELECTOR, "#linkWrapper a")

    # Print the text of each link
    print("All link texts found on the page:")
    for link in all_links:
        print("-", link.text)
finally:
    driver.quit()
