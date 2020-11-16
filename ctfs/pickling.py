import pickle
import requests

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
r = requests.get(url)
with open('banner.p', 'wb') as pickled:
    pickled.write(r.content)
    unpickled = pickle.loads(r.content)
    print(unpickled)

