import requests
from bs4 import BeautifulSoup
import re

def convert_weird_stuff_to_url(url): # it is list according to re.findall output
	a_dict = {
	'\\3A': ':',
	'\\2E': '.',
	'\\3F': '?',
	'\\2D': '-',
	'\\26': '&',
	'\\3D': '=',
	'\\2F': '/',
	' ': ''
	}
	for i in a_dict:
		for index, j in enumerate(url): 
			if i in j:
				url[index] = j.replace(i, a_dict[i])

	return url

def find_filename_from_url_and_download(url): # should be list cuz it's re.findall return as well # todo, download from here cuz it will get less confusing since this is one time using script
	r = requests.get(url)
	cd = r.headers.get('content-disposition')
	filename = re.findall('filename="([^"]*)', cd)[0]
	# url[index] = filename

	open(filename, 'wb+').write(r.content)

	return filename


# 	p1 = ["\\\\3A ",":"]
# p2 = ["\\\\2E ","."]
# p3 = ["\\\\3F ","?"]
# p4 = ["\\\\2D ","-"]
# p5 = ["\\\\26 ","&"]
# p6 = ["\\\\3D ","="]
# p7 = ["\\\\2F ","/"]
# p8 = ["",""]
# p9 = ["",""]
def download_files(url_book, format_book, name_book, chosen_format): # cuz this is after the parsing, the input would be LIST OF LIST
	for _ignore1, _ignore2, name in zip(url_book, format_book, name_book): # name is going to be a list with an item in a list
		for url, f_format in zip(_ignore1, _ignore2):
			if chosen_format == f_format:
				pass

def main():
	url = 'https://ohnotype.co/'
	font_name = 'Vulf Mono'
	chosen_format = 'woff2'

	font_url = []
	font_file_name = []
	font_style = []
	font_weight = []
	font_format = []
	#regex_in_quote = r"'([^"]*)'"
	
	print('Requesting from website!')
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	
	print('Filtering HTML code!')
	target = soup.find_all('style')

	count = 1
	print('Downloading!')
	for i in target:
		i = str(i)
		if font_name in i:
			url = convert_weird_stuff_to_url(re.findall("url[(]'([^']*)'", i))
			file_format = re.findall("format[(]'([^']*)'", i)

			for url, f in zip(url, file_format):
				if chosen_format == f:
					print(f'Got {find_filename_from_url_and_download(url)}')

			#font_file_name.append(find_filename_from_url(url))

			count +=1
			# font_url.append(url)
			# font_style.append(re.findall('font-style: ([a-z]*);', i))
			# font_weight.append(re.findall('font-weight: ([0-9]*);', i))
			# font_format.append(re.findall("format[(]'([^']*)'", i))

if __name__ == '__main__':
	main()
