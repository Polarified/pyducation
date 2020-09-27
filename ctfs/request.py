import requests

params = {'action': 'request'}
cookies = {'WC': '12874576-53802-PSwNLCkR3wkn8rbb'}
r = requests.get("https://www.wechall.net/challenge/training/programming1/index.php", params=params, cookies=cookies)
answer = r.content
params = {'answer': answer}
p = requests.get("https://www.wechall.net/challenge/training/programming1/index.php", params=params, cookies=cookies)
print(p.content)