from bs4 import BeautifulSoup
import requests
# from datetime import date
import time
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib


# Function to get the price by webscraping :---------------------------

def get_price(site_link):
    item_price = 0
    site = requests.get(site_link)
    text = site.content
    soup = BeautifulSoup(text, "html.parser")

    try:
        rate = soup.find("span", class_='a-price-whole').text
        rate = rate.replace(",", "")  # rate is a string
        for i in range(len(rate)):
            if rate[len(rate) - 1] == ".":
                error_dot = True
                rate = rate.replace(".", '')
        # print(int(rate))
        item_price = rate
        pass

    except AttributeError:
        item_price = None

    return int(item_price)


# Function to get the name of the item :---------------------------------

def get_name(site_link):
    item_name = site_link.split("/")
    item_name = item_name[3]
    # print(item_name)
    item_name = item_name.split('-')
    item_name = ' '.join(item_name)
    return item_name


# FUNCTION to send the mail to user :--------------------------------------

def send_mail(sender, password, receiver, body, subject):
    em = EmailMessage()

    em['from'] = sender
    em['to'] = receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())


# main code ------------------------------------------------------------
site_link = "https://www.amazon.in/Fire-Boltt-Phoenix-Bluetooth-Calling-Monitoring/dp/B0B3RSDSZ3/ref=sr_1_1?pd_rd_r=c56aadac-3913-42ab-a913-fea6f1c06134&pd_rd_w=j5uwe&pd_rd_wg=ZCTVE&pf_rd_p=e4a82488-6667-4629-b7da-4673cd2ae2c3&pf_rd_r=7CVYT8V1QX4SRSM6R3FW&sr=8-1&th=1"

title = get_name(site_link)
current_price = get_price(site_link)

password = "YOUR GMAIL 'APP PASSWORD'"
body = f"Price of the item '{title}' has dropped to {current_price}, click here to buy {site_link}"

original_price = 1799 # the current price of the item

while True:
    try:
        print("done----")
        if original_price > int(current_price):
            send_mail(sender="SENDER EMAIL", password=password, body=body,
                      receiver="RECEIVER EMAIL", subject="price of an item in your wishlisht has dropped.")
            pass
        pass

    except TypeError:
        print(None)

    time.sleep(300)  # AFTER every 300 seconds the code checks for the price
    pass
