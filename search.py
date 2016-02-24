import requests, json
Query = input('Query: ')
p = {'q' : Query}
response = requests.get('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&', params = p)
j = response.json()
results = j['responseData']['results']
for r in results:
	title = r['titleNoFormatting']
	url = r['url']
	print(title + ' ; ' + url)