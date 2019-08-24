import requests
from bs4 import BeautifulSoup
import smtplib

URL= 'https://www.amazon.de/V-H-Hawaiihemd-Kurzarm-violett/dp/B07Q4DZ833?pf_rd_p=2b0ccb52-55a3-4ead-8cd7-c5e4263261a5&pd_rd_wg=Kiyxs&pf_rd_r=4SEH8N5VEEN48DB8RPCQ&ref_=pd_gw_unk&pd_rd_w=xyBVB&pd_rd_r=a5dfb418-1391-4a35-a657-a51add702f64'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')
    soup1 = BeautifulSoup(soup.prettify(), "html.parser")


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    # if(converted_price < 7,00)
    #     send_mail():


    print(converted_price, '€')
    print(title)

    if(converted_price < 1.700):
        send_mail()

 def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


#in line 39 we enter our email username as well as password within the second parantheses 

    server.login('', '')

    subject = 'Price fell down'
    body = 'Check the amazon link https://www.amazon.de/V-H-Hawaiihemd-Kurzarm-violett/dp/B07Q4DZ833?pf_rd_p=2b0ccb52-55a3-4ead-8cd7-c5e4263261a5&pd_rd_wg=Kiyxs&pf_rd_r=4SEH8N5VEEN48DB8RPCQ&ref_=pd_gw_unk&pd_rd_w=xyBVB&pd_rd_r=a5dfb418-1391-4a35-a657-a51add702f64'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36     '

    msg = f"Subject": {subject} \n\n{body}
    server.sendmail('owaishassan786@gmail.com', 'owaishassan786@gmail.com', msg)
    print('Hey email has been sent')
    server.quit()

check_price()
