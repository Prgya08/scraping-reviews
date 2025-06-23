from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv
import time


options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service( r"C:\Users\pragy\OneDrive\Desktop\review selenium project\drivers\chromedriver.exe"), options=options)


driver.get("https://www.elpasosmokeshops.com/locations/")
time.sleep(2)


for _ in range(6):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)


headings = driver.find_elements(By.TAG_NAME, "h2")
store_names = []

for h in headings:
    name = h.text.strip()
    if name.endswith("Smoke Shop"):
        store_names.append(name)

print(f"\n✅ Found {len(store_names)} stores:")
for name in store_names:
    print("-", name)


def get_google_reviews(store_name):
    maps_url = "https://www.google.com/maps"
    driver.get(maps_url)
    time.sleep(3)

    
    try:
        consent = driver.find_element(By.XPATH, '//button[.="Accept all"]')
        consent.click()
        time.sleep(2)
    except:
        pass

    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchboxinput"))
        )
        search_box.clear()
        search_box.send_keys(store_name + " El Paso TX")
        search_box.send_keys(Keys.RETURN)
        print(f"🔍 Searching on Maps for {store_name}")
        time.sleep(5)

        
        try:
            review_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, " reviews")]'))
            )
            review_button.click()
            time.sleep(3)
        except:
            print(f"⚠️ Could not click 'View all reviews' for {store_name}")
            return []

        
        for _ in range(5):
            driver.execute_script("document.querySelector('div[role=\"main\"]').scrollBy(0, 300);")
            time.sleep(1)

        
        review_elements = driver.find_elements(By.CSS_SELECTOR, 'span.wiI7pd')
        reviews = [r.text.strip() for r in review_elements if r.text.strip()]
        return reviews

    except Exception as e:
        print(f"❌ Failed to get reviews for {store_name}: {e}")
        return []



all_reviews = []

for name in store_names:
    print(f"\n🔍 Searching for reviews of: {name}")
    reviews = get_google_reviews(name)
    print(f"✅ Found {len(reviews)} reviews.")
    for review in reviews:
        all_reviews.append([name, review])


with open("reviews.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Store Name", "Review"])
    writer.writerows(all_reviews)

print("\n✅ All reviews saved to reviews.csv")


driver.quit()
