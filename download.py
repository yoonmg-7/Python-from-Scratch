# from urllib.request import urlretrieve;

# link = input('Download Image link :')
# fileName = input('Image name :')

# urlretrieve(link,'image/'+fileName+'.jpg')

from urllib.request import build_opener, install_opener, urlretrieve
import os

link = input('Download Image link :')
fileName = input('Image name :')

# make sure the "image" folder exists
os.makedirs("image", exist_ok=True)

# set User-Agent for all requests
opener = build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
install_opener(opener)

urlretrieve(link, 'image/' + fileName + '.jpg')
print("Download complete!")
