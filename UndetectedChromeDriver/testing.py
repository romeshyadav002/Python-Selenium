import undetected_chromedriver as uc

# Check version
print("undetected-chromedriver version:", uc.__version__)

# Launch undetected Chrome
driver = uc.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box and type the query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")

# Keep browser open
# input("Press Enter to close...")
# driver.quit()
