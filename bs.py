import requests
import bs4
from urllib.parse import urlparse

links = ['https://www.vishalpandey.xyz']

output = ['https://www.vishalpandey.xyz']

vlinks = []

def search(theLink):
	vlinks.append(theLink)
	res = requests.get(theLink)
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	hi = soup.select('a')
	
	for x in hi:
		if 'href' in x.attrs:	
			link = x['href']
			linko = urlparse(link)
			if link[0:4] == 'http':
				slink = linko.scheme+'://'+linko.netloc
				if slink in links:
					pass
				else:
					links.append(slink)
					output.append(slink)
					fo = open("output.html", "w")
					fo.write(str(vlinks))
					fo.close()

	del links[0]
	if len(links)>0:
		if links[0] not in vlinks:
			search(links[0])
	else :
		return

search(links[0])


print(output)
print(len(output))