import time
import requests

# URL of your Render application
url = 'https://crisprbac.onrender.com'

while True:
    try:
        response = requests.get(url)
        print(f"Pinged {url}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error pinging {url}: {e}")
    # Wait for 14 minutes (14 * 60 seconds)
    time.sleep(14 * 60)
