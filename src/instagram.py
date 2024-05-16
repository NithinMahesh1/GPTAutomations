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

    # Check for "save your login info" popup dialog
    if(WebDriverWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mount_0_0_\/G > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > section > div > button')))):
        saveInfo = findElements(driver,"#mount_0_0_\/G > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > section > div > button","selector")
        saveInfo.click()
    
    if(WebDriverWait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1')))):
        notNow = findElements(driver, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1", "selector")
        notNow.click()



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
