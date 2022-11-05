from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from myLogger import Logger
# # Start the browser and login with standard_user
# def login (user, password):
#     print ('Starting the browser...')
#     # --uncomment when running in Azure DevOps.
#     # options = ChromeOptions()C
#     # options.add_argument("--headless") 
#     # driver = webdriver.Chrome(options=options)
#     driver = webdriver.Chrome(Chrome)
#     print ('Browser started successfully. Navigating to the demo page to login.')
#     driver.get('https://www.saucedemo.com/')

# login('standard_user', 'secret_sauce')

# !/usr/bin/env python6
from multiprocessing.sharedctypes import Value
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located

# from selenium.webdriver.chrome.options import Options as ChromeOptions
# driver = webdriver.Firefox(options=options, service=service)
# Start the browser and login with standard_user
# def login(user, password):
def login(user,password):
    a = Logger()
    a.setLog('info','****Iniciando el log*****')
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    url =  'https://www.saucedemo.com'
    # url = 'http://automationpractice.com/index.php'
    print ('Browser started successfully. Navigating to the demo page to login.')
    a.setLog('info','Browser started successfully. Navigating to the demo page to login.')
    # a.setLog('info',f'{url}') //da un error al poner una url
    driver.get(url)
    # driver.implicitly_wait(1.5)
    title = driver.title
    print(title)
    driver.implicitly_wait(10.0)
    inventory = []
    print(f'The user {user} is logging')
    a.setLog('info',f'The user {user} is logging')

    driver.find_element(by=By.CSS_SELECTOR,value='input[id="user-name"]').send_keys(user)
    print(f'Writing the password')
    a.setLog('info',f'Writing the password')

    driver.find_element(by=By.CSS_SELECTOR,value='input[id="password"]').send_keys(password)
    print('Clicking in login button')
    a.setLog('info','Clicking in login button')

    driver.find_element(by=By.CSS_SELECTOR,value='input[id="login-button"]').click()
    assert 'https://www.saucedemo.com/inventory.html' == driver.current_url
    # print(driver.find_element(by=By.CSS_SELECTOR,value='a[id="logout_sidebar_link"]'))
    print('Logged successfully!')
    a.setLog('info','Logged successfully!')

    print(driver.current_url)
    compras(driver,a)
    return driver

def compras(driver,a):
    
    inventory = []
    elementos = driver.find_elements(by=By.CLASS_NAME,value='btn.btn_primary.btn_small.btn_inventory')
    cantidad = len(elementos)
    elem = driver.find_elements(by=By.CLASS_NAME,value='inventory_item_name')
    print(f'There are {cantidad} products to buy.')
    a.setLog('info',f'There are {cantidad} products to buy.')
    for n in range(cantidad):
        if 'ADD' in elementos[n].text:
            print(f'Product ({elem[n].text}) added to cart.')
            a.setLog('info',f'Product ({elem[n].text}) added to cart.')
            elementos[n].click()
            inventory.append(n)

    
    
    print(elem[0].text)

    badge = driver.find_element(by=By.ID,value='shopping_cart_container')
    if int(badge.text) == cantidad:
        mensaje = '''All products add to cart
-----------------------------------------------
Removing products from cart'''
        a.setLog('info','removing products from cart')
        print(mensaje)


    #     print('All products added to cart')
    # print('----------------------------------------------')
    # print('Removing products from cart')
    elementos = driver.find_elements(by=By.CLASS_NAME,value='btn.btn_secondary.btn_small.btn_inventory')

    print(elementos[0].text)
    for n in range(cantidad):
        # if 'ADD' not in n.text:
        print(f'Removing ({elem[n].text}) product from cart')
        a.setLog('info',f'Removing ({elem[n].text}) product from cart')
        elementos[n].click()
        # inventory.pop()
    print(badge.text,'---------------------')
    a.setLog('info',f"{badge.text}-------------------")
    assert badge.text == ''
    if badge.text == '':
        message = '''All products has been remove
UI test has been passed!'''
        print(message)
        a.setLog('info','All product has been remove. UI test passed!')
    
    
    return driver
driver = login('standard_user', 'secret_sauce')

