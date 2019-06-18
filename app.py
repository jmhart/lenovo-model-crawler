import requests
import json

url = "https://support.lenovo.com/us/en/api/mse/getproducts?productId=10FVS0KX01"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers).json()

print(response[0]["Name"])
