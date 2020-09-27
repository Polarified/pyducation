import requests
from bs4 import BeautifulSoup
import zipfile

wordlist = "https://www.hackthissite.org/missions/prog/1/wordlist.zip"
cookies = {"PHPSESSID": "8i2tflmofrd011c21i3qh27bg3"}
index = "https://www.hackthissite.org/missions/prog/1/index.php"

r = requests.get(wordlist, auth=("polarified", "HsHs3yFH4,De?cJ"), allow_redirects=True)
open("wordlist.zip", 'wb').write(r.content)
with zipfile.ZipFile("wordlist.zip", 'r') as zip_ref:
    zip_ref.extractall(".")

r = requests.get(index, auth=("polarified", "HsHs3yFH4,De?cJ"), cookies=cookies)
soup = BeautifulSoup(r.text, 'html.parser')

scrambles = [li.text for li in soup.find_all("table")[-1].find_all("li")]
print(scrambles)
sorts = [''.join(sorted(scramble)) for scramble in scrambles]
print(sorts)
words = open("wordlist.txt", "r").readlines()
answers = [word[:-1] for s in sorts for word in words if ''.join(sorted(word[:-1])) == ''.join(sorted(s))]
print(answers)

r = requests.post(index, auth=("polarified", "HsHs3yFH4,De?cJ"), cookies=cookies, data={"solution": ','.join(answers)},
                  headers={'referer': index})

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
