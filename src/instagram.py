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
from chatAPI import main as chat_main

def main(fileDir,api_key):
    # Get the directory of the current file (src)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the root directory of the repository (one level up from src)
    repo_root_dir = os.path.dirname(current_dir)

    # Define the path to the UserData directory in the root of the repo
    userDataDir = os.path.join(repo_root_dir, "UserData")

    # Setup options for driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(f"user-data-dir={userDataDir}")
    options.add_argument('--profile-directory=Profile 1')
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    ]
    options.add_argument(f'user-agent={random.choice(user_agents)}')

    driver(options,fileDir,api_key)


def driver(options,fileDir,api_key,username,password):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com/")
    time.sleep(randomTimer("long"))

    # Grab Login form Elems
    usernameField = findElements(driver,'[aria-label="Phone number, username, or email"]',"selector")
    passwordField = findElements(driver,'[aria-label="Password"]',"selector")
    loginButton = findElements(driver,"#loginForm > div > div:nth-child(3) > button","selector")

    # Input fields and submit
    time.sleep(randomTimer("medium"))
    sendKeys(usernameField,username)
    time.sleep(randomTimer("short"))
    sendKeys(passwordField,password)
    time.sleep(randomTimer("medium"))
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


    time.sleep(randomTimer("long"))

    # Wait for the file input element to be present and upload the file
    keyboard = Controller()
    keyboard.type(fileDir)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # After uploading picture we click next
    time.sleep(randomTimer("long"))
    try:
        nextButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
    except:
        try:
            nextButton = driver.findElements(driver,"//div[@role='button' and contains(text(), 'Next')]", "XPATH")
        except:
            nextButton = driver.findElements(driver,"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div > div > div > div._ap97 > div > div > div > div._ac7b._ac7d > div > div", "selector")
    nextButton.click()

    # Here it asks for filters
    time.sleep(randomTimer("medium"))
    nextButton.click()

    time.sleep(randomTimer("long"))

    # TODO add logic here to type in inputs for post captions
    # Once captions are uploaded we need to click next
    # Also where chatGPT will run its logic
    chatGPTInput = chat_main(fileDir,api_key)
    captionsInputField = findElements(driver,'[aria-label="Write a caption..."]',"selector")
    captionsInputField.send_keys(chatGPTInput)


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
        time.sleep(randomTimer("short"))
        elem.send_keys(char)


# def clickElements():