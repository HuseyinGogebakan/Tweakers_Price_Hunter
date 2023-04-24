from bs4 import BeautifulSoup
import requests

print(" _____  __      __  ___     _     _  __  ___   ___   ___         _  _   _   _   _  _   _____   ___   ___ ")
print("|_   _| \ \    / / | __|   /_\   | |/ / | __| | _ \ / __|       | || | | | | | | \| | |_   _| | __| | _ \\")
print("  | |    \ \/\/ /  | _|   / _ \  | ' <  | _|  |   / \__ \       | __ | | |_| | | .` |   | |   | _|  |   /")
print("  |_|     \_/\_/   |___| /_/ \_\ |_|\_\ |___| |_|_\ |___/       |_||_|  \___/  |_|\_|   |_|   |___| |_|_\\")


print("select the procent you wanna look?")
while(True):
 print("from: ")
 below = input()
 print("to: ")
 up = input()
 if up >=below:
   break
print("any additonal filters?")
print("such as:")
url = "https://tweakers.net"
response = requests.get(url)

html = response.content

soup  = BeautifulSoup(html,"html.parser")
all_lis = soup.find_all("li")
first_eight = all_lis[:8]

for link in first_eight:
   url_each = link.a['href']
   response = requests.get(url_each)
   html = response.content
   soup = BeautifulSoup(html,"html.parser")


