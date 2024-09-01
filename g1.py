import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from chromedriver_autoinstaller import install

driver = webdriver.Chrome()

while True: #Loop to start new search
    text2search = input('Enter your text: ')

    #Error capturing 1
    try:
        driver.get("https://www.google.com/")
    except Exception as e:
        print(f"Error: The path might be incorrect. Please review the path. Reason: {e}")
        exit()

    #Error capturing 2
    try:
        assert "Google".lower() in driver.title.lower()
    except AssertionError:
        print("Error: Please verify if the webpage is displaying correctly.")
        exit()

    search_box_Xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea'

    sb = driver.find_element(By.XPATH, search_box_Xpath)
    sb.send_keys(text2search)
    sb.send_keys(Keys.ENTER)







