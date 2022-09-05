import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4, lxml
import os


class Proxy:

	"""
	simple example:
		p = Proxy()
		proxies_list = p.get_selected_proxies()
		...
		p.update()  # update file with proxies

	another example:
		p = Proxy(protocol='https', google=True, anon='elite', region='CA')
		p.get_selected_proxies() # proxies list from cache (or update cache file)
		...
		p.update()  # update file with proxies

	possible values:
		protocol['http', 'https', None]
		google[True, False, None]
		anon['elite', 'transparent', 'anonymous', None]
		region['CA', 'US', 'AU', 'RU', ... , None]
	"""

	def __init__(self, protocol: str=None, google:bool=None, anon:str=None, region:str=None):

		if protocol:
			self.protocol = protocol
		if google:
			self.google = 'google+'
		elif google == False:
			self.google = 'google-'
		if anon:
			self.anon = anon
		if region:
			self.region = region

	@classmethod
	def __parse_the_page(cls,r: requests.Response) -> str:
		soup = BeautifulSoup(r.text, 'lxml')
		div = soup.find_all('tr')
		cnt = 0
		lines = ''
		for i in div:
			cnt+=1
			td = i.find_all('td')
			if len(td) > 0:
				IP = td[0].text
				PORT = td[1].text
				CODE = td[2].text
				COUNTRY = td[3].text
				ANON = td[4].text
				GOOGLE = 'google+' if td[5].text == 'yes' else 'google-'
				HTTPS = 'https' if td[6].text == 'yes' else 'http' 
				LAST_CHECKED = td[7].text
				lines += f'{IP}:{PORT} {CODE} {COUNTRY} {ANON} {GOOGLE} {HTTPS} {LAST_CHECKED}\n'
			if cnt == 301:
				return lines

	@classmethod
	def __get_page(cls) -> requests.Response:
		url = 'https://free-proxy-list.net'
		r = requests.get(url)
		return r

	def get_selected_proxies(self) -> list:
		"""returns the proxy list"""
		if os.path.exists('all_proxies.txt'):
			text = Proxy.__get_proxies_from_file()
		else:
			self.update()
			text = Proxy.__get_proxies_from_file()
		proxies = []
		attrs = dict(self.__dict__.items())
		for string in text.split('\n'):
			attr_cnt = 0
			if string:
				for key in attrs:
					if attrs[key]+' ' in string and attrs[key] and len(attrs) != 0:
						attr_cnt+=1
						if attr_cnt == len(attrs):
							proxies.append(string.split()[0])
				if len(attrs) == 0:
					proxies.append(string.split()[0])
		return proxies

	@classmethod
	def __save_to_file(cls, data) -> None:
		with open('all_proxies.txt', 'w') as f:
			f.write(data)

	def update(self) -> None:
		response = Proxy.__get_page()
		data = self.__parse_the_page(response)
		Proxy.__save_to_file(data)

	@classmethod
	def __get_proxies_from_file(cls) -> str:
		with open('all_proxies.txt', 'r') as f:
			return f.read()

