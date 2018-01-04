import requests, os, sys, bs4


url = 'http://www.santabanta.com/photos/3-d/2110782.htm'
os.makedirs('Images')
while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    #Find url of image
    imageELE = soup.select('#wall')
    if imageELE == []:
        print('No image')
    else:
        imageURL = imageELE[0].get('src')
    
    #Downloading the image
    res = requests.get(imageURL)
    res.raise_for_status()

    #Saving the image
    imageFile = open(os.path.join('Images',os.path.basename(imageURL)),'wb')
    for chunk in res.iter_content(10000):
        imageFile.write(chunk)
    imageFile.close()

    #Get next button's URL
    nextLink = soup.select('#wall_next')[0]
    url = 'http://www.santabanta.com' + nextLink.get('href')
print('Done')