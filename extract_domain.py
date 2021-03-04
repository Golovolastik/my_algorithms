#  Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string. 

url1 = "http://github.com/golovolastik"
url2 = "www.xakep.ru"
url3 = "www.xxx-yyy.net"

def domain_name(url):
	import re
	pattern = re.compile('([\w\-]+)\.([\w\-]+)')
	result = re.search(pattern, url)
	if result.group(1) == 'www':
		return result.group(2)
	else:
		return result.group(1)	

print(domain_name(url1))
print(domain_name(url2))
print(domain_name(url3))
