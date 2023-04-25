from bs4 import BeautifulSoup
import requests

print(" _____  __      __  ___     _     _  __  ___   ___   ___         _  _   _   _   _  _   _____   ___   ___ ")
print("|_   _| \ \    / / | __|   /_\   | |/ / | __| | _ \ / __|       | || | | | | | | \| | |_   _| | __| | _ \\")
print("  | |    \ \/\/ /  | _|   / _ \  | ' <  | _|  |   / \__ \       | __ | | |_| | | .` |   | |   | _|  |   /")
print("  |_|     \_/\_/   |___| /_/ \_\ |_|\_\ |___| |_|_\ |___/       |_||_|  \___/  |_|\_|   |_|   |___| |_|_\\")


print("select the procent you wanna look?")
while(True):
 below = input("from: ")
 
 up = input("to: ")
 if up >=below:
   break
 


print("any additonal filters?")
print("such as:")

quality = "X"
price = "X"
delivery = "X"

while(True):
 option = input("1.Quality 2.Price 3.Delivery time 4.exit") or "X"
 
 if option == "X" or option == "4":
     break
 elif option == "1":
   quality = input("enter the quality as star")
 elif option == "2":
   price = input("enter the below limit")
 elif option == "3":
   delivery = input("enter min delivery time")
 else: print("you have entered invalid value pls try again")
   

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
   slider_pr = soup.find('div', {'class': 'sliderControl'})

   slider_width = int(slider_pr.find('div', {'class': 'sliderArea'})['style'].split('width: ')[1].split('px')[0])
   valuebelow= int(slider_width * (below/ 100))
   valueup= int(slider_width * (up/ 100))


   slider_pr.find_all('div', {'class': 'sliderPointer'})[0]['style'] = f'left: {valuebelow}px;'
   slider_pr.find_all('div ', {'class ': 'sliderPointer '})[1]['style'] = f'left: {valueup}px;'

   