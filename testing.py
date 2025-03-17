from selenium import webdriver

def first_test_script():
   # Create an instance of the Chrome WebDriver
   # you can use other browsers too
   driver = webdriver.Chrome()

   # navigate to the website
   driver.get("https://www.tutorialspoint.com")

   # Get the actual title of the page
   title = driver.title

   # Print the title of the website
   print("Title: " + title)
    
   # Close the browser window
   driver.quit()

if __name__ == "__main__":
   first_test_script()