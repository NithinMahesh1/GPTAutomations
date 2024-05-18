import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("user-data-dir=")
    options.add_argument('--profile-directory=Profile 1')
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    ]
    options.add_argument(f'user-agent={random.choice(user_agents)}')

    driver(options)


def driver(options):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com/")
    time.sleep(randomTimer("long"))

    # Grab Login form Elems
    usernameField = findElements(driver,'[aria-label="Phone number, username, or email"]',"selector")
    passwordField = findElements(driver,'[aria-label="Password"]',"selector")
    loginButton = findElements(driver,"#loginForm > div > div:nth-child(3) > button","selector")

    # Input fields and submit
    usernameInput = ""
    passwordInput = ""

    time.sleep(randomTimer("medium"))
    sendKeys(usernameField,usernameInput)
    sendKeys(passwordField,passwordInput)

    loginButton.click()

    # Random scrolling
    # if(ifScroll()):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Locate and click the "Create" button
    time.sleep(randomTimer("long"))
    try:
        createButton = findElements(driver, '[aria-label="New post"]', "selector")
    except:
        createButton = findElements(driver, '//span[text()="Create"]', "XPath")

    createButton.click()

    # Wait for the "Select from computer" button to be clickable and then click it
    time.sleep(randomTimer("medium"))
    selectButton = driver.find_element(By.XPATH, '//button[@type="button" and text()="Select from computer"]')
    selectButton.click()


    time.sleep(randomTimer("medium"))

    # Wait for the file input element to be present and upload the file
    fileInput = driver.find_element(By.XPATH, '//input[@type="file"]')
    fileInput.click()
    keyboard = Controller()
    keyboard.type("")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # After uploading picture we click next
    time.sleep(randomTimer("medium"))
    nextButton = driver.find_element(By.XPATH, '//button[@role="button" and text()="Next"]')
    nextButton.click()

    # TODO add logic here to type in inputs for post captions
    # Once captions are uploaded we need to click next
    # Also where chatGPT will run its logic
    nextButton.click()

    time.sleep(randomTimer("medium"))



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


def randomTimer(type):
    count = 0
    if(type == "short"):
        list = [0.1,2,0.2,3,0.3,5,7,0.4,4,0.4,3,0.5,3.2,4.6,0.6,5,0.7,2,0.7,0.8,0.9]
        count = random.choice(list)
    if(type == "medium"):
        list = [1,2,3,4,5,6,7]
        count = random.choice(list)
    if(type == "long"):
        list = [7,8,9,10,11,12,13]
        count = random.choice(list)

    return count


def ifScroll():
    yesOrNo = ["True","False"]
    isScroll = random.choice(yesOrNo)
    
    return isScroll


def sendKeys(elem,keys):
    for char in keys:
        randomTimer("short")
        elem.send_keys(char)


# def clickElements():