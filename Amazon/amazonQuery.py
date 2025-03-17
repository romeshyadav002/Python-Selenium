from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

query = 'laptop'
driver.get(f"https://www.amazon.in/s?k={query}&crid=1Q8DB29MN2UBD&sprefix=laptop%2Caps%2C252&ref=nb_sb_noss_2")

elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.text)

input("Press Enter to close the browser...")  
driver.quit()