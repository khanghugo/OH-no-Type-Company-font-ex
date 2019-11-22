import requests
from bs4 import BeautifulSoup

target = "Vulf"
tagging = '</style>, '
fonttype = " format('woff')"
url = 'https://ohnotype.co/blog/the-process-of-vulf-sans'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

finding = soup.findAll(tagging[2:-3])

splitting = str(str(finding).split(tagging)).split(fonttype)

matching = [m for m in splitting if target in m][:-1]

processed = [""]

p1 = ["\\\\3A ",":"]
p2 = ["\\\\2E ","."]
p3 = ["\\\\3F ","?"]
p4 = ["\\\\2D ","-"]
p5 = ["\\\\26 ","&"]
p6 = ["\\\\3D ","="]
p7 = ["\\\\2F ","/"]
p8 = ["",""]
p9 = ["",""]

for i in matching:
	killing = i[-250:-1].replace("'", "").replace("(", "")

	replacing = killing.replace(p1[0],p1[1]).replace(p2[0],p2[1]).replace(p3[0],p3[1]).replace(p4[0],p4[1]).replace(p5[0],p5[1]).replace(p6[0],p6[1]).replace(p7[0],p7[1])

	processed.append(replacing)

print(processed)