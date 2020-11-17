import urllib.request

nothing = '12345'
for i in range(400):
    response = urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}')
    html = str(response.read())
    print(html)
    nothing = html.split()[-1]

