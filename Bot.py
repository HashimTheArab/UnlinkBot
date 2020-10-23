from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

email = input('Input the account email.\n')
password = input('Input the account password\n')

geckopath = "./geckodriver.exe"

browser = webdriver.Firefox(executable_path=geckopath)
wait = WebDriverWait(browser, 15)
i = 0
print('Opening Microsoft.')
try:
    try:
        browser.get('https://account.microsoft.com/devices/content')
        browser.find_element_by_name('loginfmt').send_keys(email)
        browser.find_element_by_id('idSIButton9').click()
        print('Email succeeded.')
    except:
        print('Email failed.')
    try:
        browser.find_element_by_id('i0118').send_keys(password)
        browser.find_element_by_id('idSIButton9').click()
        print('Password succeeded!')
    except:
        print('Password failed.')
    print('Are you signed in? (Y/N)')
    x = input()
    if x.lower() == 'y':
        print('Starting the unlink process.')
        while i < 10:
            i += 1
            try:
                wait.until(EC.visibility_of_element_located((By.NAME, 'app-devices-unlink')));
                browser.find_element_by_name('app-devices-unlink').click()
            except:
                print(f"Failed to click the unlink button on attempt {i}.")
                break
            try:
                browser.find_element_by_name('unlink-confirm-button').click()
                print(f"Unlinked account {i}/10")
                browser.refresh()
            except:
                print(f"Failed to click the confirm button on attempt {i}.")
                break
        else:
            print('Finished unlinking devices')
    else:
        print('You have to be signed in and on the unlink screen idiot')
except:
    print(f"An error has occured. Attempt {i}")
