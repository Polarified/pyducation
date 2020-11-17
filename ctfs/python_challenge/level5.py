import pickle
import requests

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
r = requests.get(url)
unpickled = pickle.loads(r.content)
for row in unpickled:
    for t in row:
        print(t[0] * t[1], end='')
    print()

print(unpickled)

