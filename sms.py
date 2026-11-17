import os
import requests

AT_USERNAME = os.getenv("AT_USERNAME", "sandbox")
AT_API_KEY = os.getenv("AT_API_KEY", "")

def send_sms(phone, message):
    if not AT_API_KEY:
        print(f"Hakuna API Key, SMS haikutumwa kwa {phone}: {message}")
        return False
    
    url = "https://api.africastalking.com/version1/messaging"
    headers = {
        "apiKey": AT_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    data = {
        "username": AT_USERNAME,
        "to": phone,
        "message": message,
    }
    try:
        r = requests.post(url, headers=headers, data=data)
        print(f"SMS response: {r.status_code} - {r.text}")
        return True
    except Exception as e:
        print(f"Error kutuma SMS: {e}")
        return False
