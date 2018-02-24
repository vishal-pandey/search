import requests
import bs4
from urllib.parse import urlparse
import tldextract

links = ['https://www.vishalpandey.xyz']

def search(theLink):
	# print(theLink+" added .. \n")
	try:
		res = requests.get(theLink)
		soup = bs4.BeautifulSoup(res.text, 'lxml')
		hi = soup.select('a')
		
		for x in hi:
			if 'href' in x.attrs:	
				link = x['href']
				linko = urlparse(link)
				ext = tldextract.extract(link)
				if link[0:4] == 'http':
					if ext.subdomain == 'www':
						slink = linko.scheme+'://www.'+ext.domain+'.'+ext.suffix
					else :
						slink = linko.scheme+'://'+ext.domain+'.'+ext.suffix

					if slink not in links:
						links.append(slink)
						fo = open("output.html", "a")
						fo.write('<a href="'+slink+'">'+slink+'</a><br>')
						fo.close()
		
	except Exception as e:
		print(e)
	

for link in links:
	# print("searching .. "+link)
	search(link)
