from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Chrome Options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Launch Chrome
driver = webdriver.Chrome(options=options)

# Open Website
url = "https://www.flipkart.com/search?q=smart+watches"
driver.get(url)

# Wait for page load
time.sleep(5)
# ==============================
# INSERT YOUR SELECTORS HERE
# ==============================

PRODUCT_CONTAINER = "div[data-id]"
PRODUCT_NAME = ".atJtCj"
PRICE = "div.hZ3P6w"
RATING = "div._3LWZlK"

# ==============================

products = driver.find_elements(By.CSS_SELECTOR, PRODUCT_CONTAINER)

data = []

for product in products:

    try:
        name = product.find_element(
            By.CSS_SELECTOR,
            PRODUCT_NAME
        ).text
    except:
        name = ""

    try:
        price = product.find_element(
            By.CSS_SELECTOR,
            PRICE
        ).text
    except:
        price = ""

    try:
        rating = product.find_element(
            By.CSS_SELECTOR,
            RATING
        ).text
    except:
        rating = ""

    data.append({
        "Product Name": name,
        "Price": price,
        "Rating": rating
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel(
    "flipkart_smart_watches.xlsx",
    index=False
)

print(f"Total Products Scraped: {len(df)}")
print("Data saved to flipkart_smart_watches.xlsx")

# Keep browser open
input("\nPress Enter to close browser...")
print("Page Title:", driver.title)
print("Products Found:", len(products))
driver.quit()