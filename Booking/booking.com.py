import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json
import os

# Initialize Chrome
driver = uc.Chrome()

def scroll_to_bottom():
    """Scrolls to the bottom of the page to load more hotels."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for hotels to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break
        last_height = new_height

def scrape_booking(city, checkin_date, checkout_date):
    """Scrapes hotel details from Booking.com"""
    search_url = f"https://www.booking.com/searchresults.html?ss={city}&checkin={checkin_date}&checkout={checkout_date}"
    driver.get(search_url)
    time.sleep(6)

    print("Scrolling to load all hotels...")
    scroll_to_bottom()

    hotels = []

    hotel_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")
    print(f"Total Hotels Found: {len(hotel_elements)}")

    for hotel in hotel_elements:
        try:
            name = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='title']").text
        except:
            name = "N/A"

        try:
            price = hotel.find_element(By.CSS_SELECTOR, "span[data-testid='price-and-discounted-price']").text
        except:
            price = "N/A"

        try:
            rating = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='review-score']").text
        except:
            rating = "N/A"

        try:
            address = hotel.find_element(By.CSS_SELECTOR, "span[data-testid='address']").text
        except:
            address = "N/A"

        hotels.append({
            "name": name,
            "price": price,
            "rating": rating,
            "address": address,
            "city": city,
            "checkin": checkin_date,
            "checkout": checkout_date
        })

    # Folder Path
    folder_path = "./data/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save to JSON
    if hotels:
        json_path = os.path.join(folder_path, f"{city}_{checkin_date}_{checkout_date}.json")
        with open(json_path, "w") as json_file:
            json.dump(hotels, json_file, indent=4)

        print(f"✅ Data Saved in JSON: {json_path}")
    else:
        print("❌ No Data Found!")

# Example Call
scrape_booking("Chandigarh", "2025-03-10", "2025-03-11")

# Close Driver
# driver.quit()