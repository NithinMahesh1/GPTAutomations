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
from selenium_stealth import stealth

# TODO we need to generalize and abstract the instagram class
    # We can reuse a ton of classes from there such as randomTimer
    # Will need to comb through this code after writing it so it runs
    # Then go through and replace all the code that was simply copied from instagram.py
def main():
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

    driver(options)


def driver(options):
    driver = webdriver.Chrome(options=options)

    # Apply stealth settings
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

    driver.get("https://www.tiktok.com/@nohesigg")
    time.sleep(randomTimer("long"))

    followersLink = findElements(driver, 'span[data-e2e="followers"]', "selector")
    time.sleep(randomTimer("medium"))
    followersLink.click()
    
    userListContainer = findElements(driver, 'div.css-wq5jjc-DivUserListContainer', "selector")
    time.sleep(randomTimer("short"))
    followButtons = userListContainer.find_elements(By.CSS_SELECTOR, 'button[data-e2e="follow-button"]')

    count = 0
    for button in followButtons:
        time.sleep(randomTimer("short"))
        if(count != 40):
            time.sleep(randomTimer("short"))
            try:
                time.sleep(randomTimer("short"))
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button))
                time.sleep(randomTimer("short"))
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                # time.sleep(randomTimer("short"))
                button.click()
                # time.sleep(randomTimer("short"))
            except:
                print("failed follow button click on follower: " +count)
        count += 1

    

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
        list = [0.1,2,0.2,3,0.3,0.4,4,0.4,3,0.5,3.2,2.6,0.6,3.2,0.7,2,0.7,0.8,0.9,1.1,1.2,1.3,1.4,1.5,1.6,1.7,2.2,2.3,2.4]
        count = random.choice(list)
    if(type == "medium"):
        list = [1,2,3,4,5,6,7]
        count = random.choice(list)
    if(type == "long"):
        list = [7,8,9,10,11,12,13]
        count = random.choice(list)

    return count
