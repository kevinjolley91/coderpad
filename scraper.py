import requests

url = "https://pixelford.com/blog/"
import random
random_number = random.randint(1, 999999999999)
response = requests.get(url, headers = {'user-agent': f'Hello {random_number}'})
print(response.content)