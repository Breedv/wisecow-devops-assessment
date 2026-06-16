import requests
from datetime import datetime

URL = "http://localhost:4499"

print("=" * 50)
print("APPLICATION HEALTH CHECK")
print("=" * 50)
print(f"Timestamp: {datetime.now()}")

try:
    response = requests.get(URL, timeout=5)

    print(f"URL: {URL}")
    print(f"HTTP Status Code: {response.status_code}")

    if response.status_code == 200:
        print("Application Status: UP")
    else:
        print("Application Status: DOWN")

except Exception as e:
    print("Application Status: DOWN")
    print(f"Error: {e}")