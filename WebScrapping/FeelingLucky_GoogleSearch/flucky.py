import webbrowser, bs4, requests, sys

print('Googling...')    #display text while downloading the page

res = requests.get('http://www.google.com/search?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Retrieve top search results
soup = bs4.BeautifulSoup(res.text)

#TODO: Open a browser tab for each result
linkElements = soup.select('.r a')

for r in range(len(linkElements)):
    print(linkElements)
numOpen = min(2, len(linkElements))
for i in range(numOpen):
    webbrowser.open('http://www.google.com/'+linkElements[i].get('href'))