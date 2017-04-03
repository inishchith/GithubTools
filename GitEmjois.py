# Gives list of all EMOJIS available for use on GitHub
# saves it to a emoji.md file , use right away

import requests
import json
from bs4 import BeautifulSoup

url = "https://api.github.com/emojis"
req = requests.get(url)
data = req.json()
fi = open('emoji.md','w')
fi.write('Cool Emojis <br><br> \n')
for icon,link in zip(data.keys(),data.values()):
    fi.write(icon +'  :   ' +':'+icon+':'+'<br>\n')

print("Check emoji.md @ current directory")