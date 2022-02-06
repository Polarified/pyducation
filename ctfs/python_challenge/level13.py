import pprint
from xmlrpc import client

evil = "33888444555"
# xml = """<?xml version="1.0"?>
# <methodCall>
#    <methodName>phonethat</methodName>
#       <params>
#          <param>
#             <value><string>33888444555</string></value>
#          </param>
#       </params>
# </methodCall>"""
# headers = {'Content-Type': 'application/xml'}
# response = requests.post('http://www.pythonchallenge.com/pc/phonebook.php', data=xml, headers=headers)
# pprint.pprint(response.content)


url = 'http://www.pythonchallenge.com/pc/return/disproportional.html'
php_url = 'http://www.pythonchallenge.com/pc/phonebook.php'

s = client.ServerProxy(php_url)

print(s.system.listMethods())
print(s.system.getCapabilities())
print(s.system.methodHelp("phone"))
print(s.system.methodSignature("phone"))
# I cheated here, but only after I figured everything out! I thought it would be something cool like 33888444555,
# instead it was Bert (the name found in the previous puzzle when looking at evil4 (which I did not...)
print(s.phone("Bert"))

