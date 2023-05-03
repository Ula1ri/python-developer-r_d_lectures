import requests
import random

websites = ["https://google.com", "https://facebook.com", "https://twitter.com", "https://amazon.com", "https://apple.com"]

website = random.choice(websites)

response = requests.get(website)

print(f"Site: {website}")
print(f"Response Status Code: {response.status_code}")
print(f"Response Length: {len(response.content)}")
print(f"Response Length: {response.content}")