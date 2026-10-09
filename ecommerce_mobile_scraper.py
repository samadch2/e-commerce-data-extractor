import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Mobile Store se data scrape ho raha hai...")
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="thumbnail")
all_mobiles = []

for product in products:
    title = product.find("a", class_="title")["title"]
    price = product.find("h4", class_="price").text.strip()
    description = product.find("p", class_="description").text.strip()
    
    # Corrected Reviews Selector
    review_el = product.select_one("div.ratings p.pull-right") or product.select_one("div.ratings p")
    reviews = review_el.text.strip() if review_el else "N/A"
    
    all_mobiles.append({
        "Mobile Name": title,
        "Price": price,
        "Description": description,
        "Reviews": reviews
    })

# Save to Excel
df = pd.DataFrame(all_mobiles)
df.to_excel("mobile_phones_data.xlsx", index=False)

print(f"\nCompleted! Total {len(all_mobiles)} Mobile Phones ka data 'mobile_phones_data.xlsx' mein save ho gaya hai.")