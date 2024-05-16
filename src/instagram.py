import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("user-data-dir=")
    options.add_argument('--profile-directory=Profile 1')

    driver(options)


def driver(options):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    # Grab Login form Elems
    usernameField = findElements(driver,'[aria-label="Phone number, username, or email"]',"selector")
    passwordField = findElements(driver,'[aria-label="Password"]',"selector")
    loginButton = findElements(driver,"#loginForm > div > div:nth-child(3) > button","selector")

    # Input fields and submit
    usernameField.send_keys("")
    passwordField.send_keys("")
    loginButton.click()

    # Locate and click the "Create" button
    time.sleep(6)
    createButton = findElements(driver, '[aria-label="New post"]', "selector")
    createButton.click()

    # Wait for the "Select from computer" button to be clickable and then click it
    time.sleep(5)
    selectButton = driver.find_element(By.XPATH, '//button[@type="button" and text()="Select from computer"]')
    selectButton.click()


    time.sleep(2)
    # Wait for the file input element to be present and upload the file
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    fileInput = driver.find_element(By.XPATH, '//input[@type="file"]')
    file_path = "C:\\Users\\vboxuser\\Desktop\\Annotation 2024-05-16 181804.png"  # Provide the full path to the image file
    fileInput.send_keys(os.path.abspath(file_path))  # Ensure the path is absolute

    # fileInput = driver.find_element(By.XPATH, '//input[@type="file"]')
    # fileInput.send_keys("C:\\Users\\vboxuser\\Desktop\\Annotation 2024-05-16 181804.png")

    time.sleep(2)
    nextButton = driver.find_element(By.XPATH, '//button[@role="button" and text()="Next"]')
    nextButton.click()
    nextButton.click()

    time.sleep(2)



def findElements(driver,input,type):
    if(type == "class"):
        elem = driver.find_element(By.CLASS_NAME, input)
    if(type == "ID"):
        elem = driver.find_element(By.ID, input)
    if(type == "XPath"):
        elem = driver.find_element(By.XPATH, input)
    if(type == "selector"):
        elem = driver.find_element(By.CSS_SELECTOR, input)
    else:
        raise ValueError(f"Unsupported locator type: {type}")

    return elem


# def clickElements():


# def fieldInputs():
