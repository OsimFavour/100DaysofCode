from requests_html import HTMLSession
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

BUY_PRICE = 200
URL = "https://www.amazon.com/Dell-Latitude-E5450-Certified-Refurbished/dp/B07CTRFHW9"

s = HTMLSession()
r = s.get(URL)
r.html.render(sleep=1, timeout=20)

product = {
    "title": r.html.xpath('//*[@id="productTitle"]', first=True).text,
    "price": r.html.xpath('//*[@id="corePrice_feature_div"]/div/span/span[2]', first=True).text
}

print(product)
price = float(product["price"].replace("$", ""))

if price < BUY_PRICE:
    # print(price)
    message = f"{product['title']} is now {product['price']} below your target price, Buy now!"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Instant Laptop Price Alert:\n\n{message}\n\n{URL}"
        )





