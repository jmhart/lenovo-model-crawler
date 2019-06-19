import requests
import json


def get_model_name(model_id):
    url = f"https://support.lenovo.com/us/en/api/mse/getproducts?productId={model_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers).json()
    except requests.exceptions.Timeout:
        return f"Timeout for model_id: {model_id}"
    except requests.exceptions.TooManyRedirects:
        return f"Too many redirects for model_id: {model_id}"
    except requests.exceptions.RequestException as e:
        return e

    if not response:
        return "No matching model_id"

    model_name = response[0]["Name"].split(" ")[0]

    return model_name
